import pygame, math

class line():
    
    def __init__(self, start, end, divisions = 3, width = 1, radius = 3, line_color = (0,0,0), point_color = (0,0,0)):
        self.start = start
        self.end = end
        self.divisions = divisions
        self.width = width
        self.radius = radius
        self.line_color = line_color
        self.point_color = point_color

        self.points = []

        self.divide()

    def divide(self):
        shift_x = (self.start[0] - self.end[0])/self.divisions
        shift_y = (self.start[1] - self.end[1])/self.divisions
        
        self.points = []

        for i in range(0, self.divisions + 1):
            self.points.append([int(self.start[0] - shift_x * i),int(self.start[1] - shift_y *i)])
    
    def draw(self, screen):
        
        for i in self.points:
            pygame.draw.circle(screen, self.point_color, i, self.radius)
        
        pygame.draw.line(screen, self.line_color, self.start, self.end, width = self.width)
    
    def move(self, pos,  start = True):

        if start:
            self.start = pos
        else:
            self.end = pos
        
        self.divide()

class curve():

    def __init__(self, end_points, division = 3, width = 1, radius = 3, cross_color = (255,0,0), edge_color = (0,0,0), point_color = (0,0,0)):
        self.end_points = end_points
        self.division = division
        self.width = 1
        self.radius = radius
        self.cross_color = cross_color
        self.edge_color = edge_color
        self.point_color = point_color

        self.lines = []

        past = None
        for i in end_points:
            if past != None:
                self.lines.append(line(past, i, self.division, self.width, self.radius, self.edge_color, self.point_color))
            past = i
    
    def move(self, point, pos):
        self.end_points[point] = pos

        if point != 0:
            self.lines[point-1].move(pos, False)
        if point != len(self.end_points)-1:
            self.lines[point].move(pos, True)

    def draw(self, screen):

        for i in self.lines:
            i.draw(screen)
        
        for i in range(len(self.lines)-1):
            for j in range(len(self.lines[i].points)-1):
                pygame.draw.line(screen, self.cross_color, self.lines[i].points[j], self.lines[i+1].points[j+1])

def dist(a, b):
    d = (a[0]-b[0])**2 + (a[1]-b[1])**2 

    return d

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720))
     
    # define a variable to control the main loop
    running = True
     
    # define colors
    WHITE = (255, 255, 255)

    ACTIVE_DIST = 100

    # create the curve
    test = curve([[100,100],[100,300],[300,300]], division=25)

    down_last = False
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if down_last == False:
            
                for i in test.end_points:
                    d = dist(i, pos)

                    if d <= ACTIVE_DIST:
                        moving = test.end_points.index(i)
            
            test.move(moving, pos)

            down_last = True
        
        else:
            down_last = False
        
        screen.fill(WHITE)

        test.draw(screen)

        pygame.display.update()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

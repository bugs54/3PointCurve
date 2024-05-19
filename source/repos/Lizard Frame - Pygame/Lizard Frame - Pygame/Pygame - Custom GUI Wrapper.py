"""
I Know that this will be very slow bc it's in python and because I'm bad at making good algorithms.
"""

"""
Listener                    ### Done ###
Picture box                 # Next Job #
Number Selector
Button                      # Next Job #
Basic Shapes                # Next Job #
Transparent Colors
Sub-Window                  ### Done ###
Scrollbar
Dropdown
Webcam feed - Pygame.camera
Window - Resizable          ### Done ###
Grid System                 ### Done ###
"""
import pygame
import pygame.camera
import os
import sys

class window():
    def __init__(self, size = (600, 480), bg = (0,0,0), name = "Window", flag = 0, grid_size = (80,45)):
        # initialize pygame
        if not pygame.get_init():
            pygame.init()
        if not pygame.display.get_init():
            pygame.display.init()
        
        # create the display
        match flag:
            case 0:
                self.screen = pygame.display.set_mode(size = size)
            case 1:
                self.screen = pygame.display.set_mode(size = size, flags= pygame.RESIZABLE)
            case 2:
                self.screen = pygame.display.set_mode(size = size, flags= pygame.FULLSCREEN)
        
        self.screen.fill(bg)
        
        pygame.display.flip()
        
        # change the name of the window
        pygame.display.set_caption(name)
        
        # create the variables needed for the rest of the class
        self.size = size
        self.name = name
        self.bg = bg
        self.sub_windows = [] # List of sub-windows.
        self.sub_rects = [] # List of rects to be updated.
        self.grid_size = grid_size # the min number of grid spaces in the vertical and horizontal.
        self.box_size = (0,0) # the size of each grid box.
        
        self.listeners = [] # list of all the listeners in the program.
        
        self.update_grid()
        
        # add the needed listeners
        self.add_listener(listener(pygame.QUIT, sys.exit))
        self.add_listener(listener(pygame.VIDEORESIZE, self.redraw))
    
    def update(self):
        
        # Update the interactive
        for event in pygame.event.get():
            for listen in self.listeners:
                
                if listen.get_type() == event.type:
                    listen.update()
            
        # Update the visual
        pygame.display.update(self.sub_rects)
        
        return True
    
    def add_listener(self, listener):
        self.listeners.append(listener)
    
    def add_sub_window(self, area):
        self.sub_windows.append(area)
     
    def redraw(self):
        self.screen.fill(self.bg)
        
        self.size = self.screen.get_size()
        
        self.update_grid()
        
        self.sub_rects = []
        for i in self.sub_windows:
            i.grid_update()
            
        pygame.display.flip()
            
    def update_grid(self):
        
        # set the size of the box so the full needed grid will fit in the window 100% of the time
        if self.size[0]/self.grid_size[0] > self.size[1]/self.grid_size[1]:
            self.box_size = self.size[1]/self.grid_size[1]
        else:
            self.box_size = self.size[0]/self.grid_size[0]
            
class listener():
    def __init__(self, event, action):
        self.type = event
        self.action = action
    
    def update(self):
        self.action()
    
    def get_type(self):
        return self.type

if __name__ == "__main__":
    TestWin = window(bg = (50,50,50), flag=1)
    
    running = True
    while running:
        running = TestWin.update()
        

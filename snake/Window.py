import pygame
import numpy as np
import random

class Window:
    def __init__(self):
        pygame.init()

        self.width = 400
        self.height = 400
        
        self.rows = 10
        self.columns = 10
        
        self.grid = np.array((self.rows, self.height))
        
        self.hasGrid = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def isCoordWithin(self, x, y):
        return x >= 0 and x < self.columns and y >= 0 and y < self.rows

    def repaint(self):
        self.screen.fill("green")
        self.paintGridLines()
        
    def quit(self):
        pygame.quit
        
    def widthGap(self):
        return self.width / self.columns
                
    def heightGap(self):
        return self.height / self.rows
    
    def colourRandom(self):
        i = random.Random().randint(0, self.columns)
        j = random.Random().randint(0, self.rows)
        self.paintCoord(i, j)
    
    def paintCoord(self, i, j, colour = "black"):
        w = self.widthGap()
        h = self.heightGap()
        pygame.draw.rect(self.screen, colour, (i * w, j * h, w, h))
        
    def paintGridLines(self):
        for c in range(self.columns):
            start_pos = (self.widthGap() * c, 0)
            end_pos = (self.widthGap() * c, self.height)
            pygame.draw.line(self.screen, "black", start_pos, end_pos, 1)
        
        for r in range(self.rows):
            start_pos = (0, self.heightGap() * r)
            end_pos = (self.width, self.heightGap() * r)
            pygame.draw.line(self.screen, "black", start_pos, end_pos, 1)

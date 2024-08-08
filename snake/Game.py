from Window import Window
import pygame
import random


class Game:
    def __init__(self):
        pass

    def run(self):
        # Main loop
        # Create Window
        window = Window()
        
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            window.repaint()
            window.clock.tick(1000000)
            
        window.quit()
        print("Quiting")

def main():
    game = Game()
    game.run()

main()
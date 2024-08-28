from Window import Window
from SnakeGame import SnakeGame
from GameCode import GameCode
import pygame

class Game:
    nullCoords = (-1, -1)
    
    def __init__(self):
        self.buffer = []
        self.clock = pygame.time.Clock()
        self.TICK_SPEED = 125

    def getEventsAndClear(self):
        events = pygame.event.get().copy()
        pygame.event.clear()
        return events

    def run(self):
        game = SnakeGame()
        status = GameCode.RUN
        
        while status == GameCode.RUN:
            events = self.getEventsAndClear()            
            status = game.handleInputs(events)
            
            game.repaint()
            pygame.display.update()
            pygame.time.delay(self.TICK_SPEED)   
            
        game.quit()
        print("Quiting")
        
def main():
    game = Game()
    game.run()

main()
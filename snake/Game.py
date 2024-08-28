from Window import Window
from SnakeGame import SnakeGame
from SnakeHomePage import SnakeHomePage, HomePageStatus
from GameCode import GameCode
import pygame

class Game:    
    def __init__(self):
        self.buffer = []
        self.clock = pygame.time.Clock()
        self.TICK_SPEED = 125
        self.window = Window()

    def getEventsAndClear(self):
        events = pygame.event.get().copy()
        pygame.event.clear()
        return events

    def run(self):
        game = SnakeGame(self.window)
        status = GameCode.RUN
    
        while status == GameCode.RUN:
            events = self.getEventsAndClear()            
            status = game.handleInputs(events)
            
            game.repaint()
            pygame.display.update()
            pygame.time.delay(self.TICK_SPEED)   
        
    def mainLoop(self):
        page = SnakeHomePage(self.window)
        action = page.run()
        if (action == HomePageStatus.GAME):
            self.run()
        # Main Page - > Returns which page
        #Main Page
        # - HighScore
        # - Settings
        # - Play
        # - Quit
        self.window.quit()
        print("Quiting")
    
def main():
    game = Game()
    game.mainLoop()

main()
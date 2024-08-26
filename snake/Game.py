from Window import Window
from SnakeGame import SnakeGame
import pygame

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.TICK_SPEED = 100

    def run(self):
        snake = SnakeGame()
        running = True
        
        while running:
            acted = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                acted = snake.react(event)
            
            if (not acted):
                snake.snake.tick()
                
            snake.repaint()
            pygame.display.update()
            pygame.time.delay(self.TICK_SPEED)   
            
        snake.quit()
        print("Quiting")
        
def main():
    game = Game()
    game.run()

main()
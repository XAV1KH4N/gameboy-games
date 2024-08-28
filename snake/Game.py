from Window import Window
from SnakeGame import SnakeGame
import pygame

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.TICK_SPEED = 125

    def run(self):
        snake = SnakeGame()
        running = True
        
        while running:
            acted = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                acted = snake.react(event)
                if acted:
                    break # add the rest to a buffer for the next "tick", events should probably expire
            
            if (not acted and snake.canSnakeMove(snake.snake.direction)):
                x, y = snake.snake.nextMove(snake.snake.direction)
                snake.snake.tick(snake.consumeApple(x, y))
                
            elif (not acted and not snake.canSnakeMove(snake.snake.direction)):
                running = False
                
            snake.repaint()
            pygame.display.update()
            pygame.time.delay(self.TICK_SPEED)   
            
        snake.quit()
        print("Quiting")
        
def main():
    game = Game()
    game.run()

main()
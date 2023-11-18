import pygame
import sys

from src import Objects
from src import settings


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("CIV")
        self.clock = pygame.time.Clock()

        self.objects = Objects()

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.objects.run()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':

    game = Game()
    game.run()

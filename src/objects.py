import pygame

from src import settings
from src.tile import GreenGrass
from src.player import Player
from src.trees import Trees


class Objects:

    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):

        for row_idx in range(int(settings.HEIGHT/settings.TILE_SIZE)):
            y = row_idx*settings.TILE_SIZE
            for col_idx in range(int(settings.WIDTH/settings.TILE_SIZE)):
                x = col_idx * settings.TILE_SIZE
                GreenGrass((x, y), (self.visible_sprites,))

    def run(self):

        self.visible_sprites.draw(self.display_surface)

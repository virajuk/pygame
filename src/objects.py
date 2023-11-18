import pygame

from src import settings
from src.tile import GreenTile1, GreenTile2, GreenTile3
from src.player import Player


class Objects:

    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):

        for row_idx, row in enumerate(settings.WORLD_MAP):
            y = row_idx*settings.TILE_SIZE
            for col_idx, col in enumerate(row):
                x = col_idx*settings.TILE_SIZE

                if col == 'x':
                    GreenTile1((x, y), (self.visible_sprites, ))

                if col == 'g2':
                    GreenTile2((x, y), (self.visible_sprites, ))

                if col == 'g3':
                    GreenTile3((x, y), (self.visible_sprites, ))

                if col == 'p':
                    Player((x, y), (self.visible_sprites, ))

    def run(self):

        self.visible_sprites.draw(self.display_surface)

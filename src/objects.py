import numpy as np

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

        self.tree_sprites = pygame.sprite.Group()

        self.create_map()
        self.create_trees()

    def create_map(self):

        self.map_size = [int(settings.HEIGHT/settings.TILE_SIZE), int(settings.WIDTH/settings.TILE_SIZE)]

        for row_idx in range(self.map_size[0]):
            y = row_idx*settings.TILE_SIZE
            for col_idx in range(self.map_size[1]):
                x = col_idx * settings.TILE_SIZE
                GreenGrass((x, y), (self.visible_sprites, ))

    def create_trees(self):

        patch_1 = (int(self.map_size[1]/4), int(self.map_size[0]/4))
        patch_2 = (int(3*self.map_size[1]/4), int(self.map_size[0]/4))
        patch_3 = (int(self.map_size[1]/4), int(3*self.map_size[0]/4))
        patch_4 = (int(3*self.map_size[1]/4), int(3*self.map_size[0]/4))

        Trees((patch_1[0]*settings.TILE_SIZE, patch_1[1]*settings.TILE_SIZE), (self.visible_sprites, self.tree_sprites))
        Trees((patch_2[0]*settings.TILE_SIZE, patch_2[1]*settings.TILE_SIZE), (self.visible_sprites, self.tree_sprites))
        Trees((patch_3[0]*settings.TILE_SIZE, patch_3[1]*settings.TILE_SIZE), (self.visible_sprites, self.tree_sprites))
        Trees((patch_4[0]*settings.TILE_SIZE, patch_4[1]*settings.TILE_SIZE), (self.visible_sprites, self.tree_sprites))

        # print(self.tree_sprites)
        # print(pygame.math.clamp(0, 2, 25))
        # print(pygame.math.lerp(0, 50, 0.3))

    def run(self):

        self.visible_sprites.draw(self.display_surface)

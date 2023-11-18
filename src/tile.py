import pygame
from src.settings import *


class GreenGrass(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/grass/green_grass_64_1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class GreenTile1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/grass/green_grass_64_1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class GreenTile2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/grass/green_grass_64_2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class GreenTile3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/grass/grass_3.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

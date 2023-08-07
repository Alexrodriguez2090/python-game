import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.surface = pygame.image.load("images/textures/ground/" + type + ".png").convert_alpha()
        self.rect = self.surface.get_rect(topleft = (x, y))


class Wall(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.surface = pygame.image.load("images/textures/ground/" + type + ".png").convert_alpha()
        self.rect = self.surface.get_rect(topleft = (x, y))
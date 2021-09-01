import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []


class Minion(pygame.sprite.Sprite):
    def __init__(self, x, y, rect_size):
        super().__init__()
        self.rect.topleft = [x, y]
        self.rect = self.image.get_rect()

    def draw(self, screen):
        pass



import pygame
import math
from Support import load_folder


class Spell(pygame.sprite.Sprite):
    def __init__(self, spell_id, x, y, mx, my):
        super().__init__()
        # position
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        # animations
        self.animations = {}
        self.load_spell_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # combat / spell info
        self.id = spell_id
        self.projectile_speed = 1
        self.spell_dict = {1: 'fireball', 2: 'ice_shard'}
        # movement math
        self.dx = self.mx - self.x
        self.dy = self.my - self.y
        if self.dx == 0:
            self.dx = 1
        self.theta = math.atan(self.dy/self.dx)
        self.x_move = math.cos(self.theta) * self.projectile_speed
        self.y_move = math.sin(self.theta) * self.projectile_speed
        self.quadrant = 4
        if self.dx < 0:    # mouse is to left of character
            if self.dy < 0:    # mouse is above character
                self.quadrant = 2
            else:  # mouse is below char
                self.quadrant = 3
        elif self.dy < 0:
            self.quadrant = 1

        print(self.quadrant)

        # pygame info
        self.image = self.animations['fireball'][self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))

    def load_spell_assets(self):
        spell_path = 'art/spells/'
        # self.animations = {'fireball': [], 'ice_shard': []}
        self.animations = {'fireball': []}

        for spell in self.animations.keys():
            full_path = spell_path + spell
            self.animations[spell] = load_folder(full_path)

    def animate(self):
        animation = self.animations[self.spell_dict[self.id]]   # Fireball

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            # self.kill()

        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)

    def move(self):
        if self.quadrant == 1:
            self.x += self.x_move
            self.y -= self.y_move
        if self.quadrant == 2:
            self.x -= self.x_move
            self.y -= self.y_move
        if self.quadrant == 3:
            self.x -= self.x_move
            self.y += self.y_move
        else:
            self.x += self.x_move
            self.y += self.y_move

    def update(self, scroll):
        self.move()
        self.rect = self.image.get_rect(center=(self.x - scroll[0], self.y - scroll[1]))
        self.animate()

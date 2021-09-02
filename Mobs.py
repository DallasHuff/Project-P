import pygame
from Support import load_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # ---- movement -----
        self.x = x
        self.y = y
        self.speed = 1.5
        self.status = 'idle'
        self.facing_right = True

        # ------- animation ------
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animations = {}
        self.load_character_assets()
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        # ----- spells -------
        self.curr_spell = 0

    def load_character_assets(self):
        character_path = 'art/mobs/lizard_m/'
        self.animations = {'idle': [], 'run': [], 'hit': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = load_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.animate()
        self.move()

    def move(self):

        k = pygame.key.get_pressed()

        # ------- controls
        self.status = 'idle'
        # movement
        if k[pygame.K_a]:
            self.x -= self.speed
            self.status = 'run'
            self.facing_right = False
        if k[pygame.K_d]:
            self.x += self.speed
            self.status = 'run'
            self.facing_right = True
        if k[pygame.K_w]:
            self.y -= self.speed
            self.status = 'run'
        if k[pygame.K_s]:
            self.y += self.speed
            self.status = 'run'
        # TODO spells


class Minion(pygame.sprite.Sprite):
    def __init__(self, x, y, rect_size):
        super().__init__()
        self.rect.topleft = [x, y]
        self.rect = self.image.get_rect()

    def draw(self, screen):
        pass

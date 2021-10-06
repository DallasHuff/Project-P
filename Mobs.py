from Support import load_folder
from SpriteGroups import *
from Spells import Spell


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, unit='lizard_m', hp=100):
        super().__init__()
        # ---- movement -----
        self.x = x
        self.y = y
        self.speed = 1.5
        self.status = 'idle'
        self.facing_right = True

        # ------- animation ------
        self.unit = unit    # lizard_m as default unit
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animations = {}
        self.spell_animations = {}
        self.load_character_assets()
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        # ----- combat -------
        self.hp = hp
        self.curr_spell = 0

    def rtn_rect(self):
        return self.rect.centerx, self.rect.centery

    def rtn_pos(self):
        return self.x, self.y

    def load_character_assets(self):
        character_path = 'art/mobs/' + self.unit + '/'
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

    def actions(self):
        # ------- controls
        self.status = 'idle'
        # movement

    def update(self, scroll):
        self.rect = self.image.get_rect(center=(self.x - scroll[0], self.y - scroll[1]))
        self.animate()
        self.actions()


class Player(Mob):
    def __init__(self, x, y, display):
        super().__init__(x, y, unit='knight_m')
        self.hp = 100
        self.spell_CD = 10
        self.spell_index = 0
        self.spell_ready = True
        self.display = display

    def actions(self):
        k = pygame.key.get_pressed()

        self.spell_index += 0.1
        if self.spell_index >= self.spell_CD:
            self.spell_index = 0
            self.spell_ready = True

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
        if k[pygame.K_1]:
            # if self.spell_ready:
            #     self.spell_ready = False
            mx, my = pygame.mouse.get_pos()
            pygame.draw.line(self.display, (255, 255, 0), (self.rect.centerx, self.rect.centery), (mx / 3, my / 3), 3)
            spell = Spell(1, self.x, self.y, mx / 3, my / 3)
            spell_sprites.add(spell)

    def load_character_assets(self):
        character_path = 'art/mobs/' + self.unit + '/'
        self.animations = {'idle': [], 'run': [], 'hit': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = load_folder(full_path)


class BigZombie(Mob):
    def __init__(self, x, y):
        super().__init__(x, y, unit='big_zombie', hp=500)

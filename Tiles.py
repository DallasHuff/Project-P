import pygame


class Tilesheet:
    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load(filename).convert()
        self.tile_table = []
        for tile_x in range(0, cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))
        self.tile_map = self.create_tile_map(width, height)

    @staticmethod
    def create_tile_map(width, height):
        tile_map = {}
        num = 0
        for c in range (0, width):
            for r in range(0, height):
                tile_map[num] = (r, c)
                print(num, tile_map[num])
                num += 1
        return tile_map

    def get_tile(self, x, y):
        return self.tile_table[x][y]

    def draw(self, screen, tile, x, y):
        pass


# tile_set = makeSprite('art/environment/dungeon_tileset.png')


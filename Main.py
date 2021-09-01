from Tiles import *
from csv import reader
import pygame
import random
import math
import sys
import time
import os


# Colors  --------------------------------------- #
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)


def load_map(path):
    game_map = []
    with open(path + '.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            game_map.append(row)
    return game_map


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def game_menu():

    for event in pygame.event.get():
        pass


def main_menu():

    click = False
    exit_button = False

    while True:

        big_screen.fill((0, 0, 0))
        draw_text('PROJECT:', title_font, (209, 67, 27), big_screen, s_width * 0.5, s_height / 10)
        draw_text('PHOENIX', title_font, (209, 67, 27), big_screen, s_width * 0.5, s_height / 5)

        button_1 = pygame.Rect(s_width * 0.4, s_height * 0.5, s_width / 5, s_height / 15)
        button_2 = pygame.Rect(s_width * 0.4, s_height * 0.65, s_width / 5, s_height / 15)
        button_3 = pygame.Rect(s_width * 0.4, s_height * 0.8, s_width / 5, s_height / 15)
        pygame.draw.rect(big_screen, (230, 138, 0), button_1)
        pygame.draw.rect(big_screen, (230, 138, 0), button_2)
        pygame.draw.rect(big_screen, (230, 138, 0), button_3)

        # ------------ testing
        screen.blit(Tileset.get_tile(1, 1), (100, 100))
        # ----------------

        draw_text('Play Game', menu_font, (255, 255, 255), big_screen, s_width * 0.5, s_height * 0.5 + s_height / 30)
        draw_text('Options (NYI)', menu_font, (255, 255, 255), big_screen, s_width * 0.5, s_height * 0.65 + s_height / 30)
        draw_text('Exit Game', menu_font, (255, 255, 255), big_screen, s_width * 0.5, s_height * 0.8 + s_height / 30)

        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)):
            if click:
                main_game()
        if button_2.collidepoint((mx, my)):
            if click:
                print('button 2')
        if button_3.collidepoint((mx, my)):
            if click:
                sys.exit('exit button')

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit('pressed escape')
        pygame.display.update()


def main_game():

    last_time = time.time()

    curr_map = load_map('art/environment/real_test')

    # Game Loop  ------------------------------------------------- #
    while True:

        # Background  -------------------------------------------- #
        dt = time.time() - last_time
        dt *= frame_rate
        last_time = time.time()

        # Button presses ----------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    main_menu()
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        # -------------- draw screen
        screen.fill((0, 0, 0))
        # -------- draw tiles
        y = 0
        for row in curr_map:
            x = 0
            for item in row:
                item = int(item)
                if item != -1:
                    r, c = Tileset.tile_map[item]
                    screen.blit(Tileset.get_tile(r, c), (x * 16, y * 16))
                x += 1
            y += 1

        # dec_scroll[0] += (player_rect.x - dec_scroll[0] - (s_width / 2))/20
        # dec_scroll[1] += (player_rect.y - dec_scroll[1] - (s_height / 2)) / 20
        pygame.display.update()
        big_screen.blit(pygame.transform.scale(screen, (s_width, s_height)), (0,0))
        dt = clock.tick(60)


if __name__ == '__main__':

    # General init ----------------------------------------------- #
    pygame.init()
    clock = pygame.time.Clock()
    frame_rate = 60

    # Font init -------------------------------------------------- #
    default_font = pygame.font.SysFont('Times New Roman', 20)
    title_font = pygame.font.SysFont('couriernew', 100)
    menu_font = pygame.font.SysFont('candara', 50)

    # Screen display info  --------------------------------------- #
    big_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    s_info = pygame.display.Info()
    s_width, s_height = s_info.current_w, s_info.current_h
    screen = pygame.Surface((s_width / 3, s_height / 3))

    Tileset = Tilesheet('art/environment/spritesheet.png', 16, 16, 16, 16)

    main_menu()
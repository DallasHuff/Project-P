import pygame

pygame.init()  # have to do this to create font
font = pygame.font.SysFont('candara', 30)


def debug(info, x=10, y=10):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, (0, 255, 0))
    debug_rect = debug_surf.get_rect(topleft=(x,y))
    display_surf.blit(debug_surf, debug_rect)

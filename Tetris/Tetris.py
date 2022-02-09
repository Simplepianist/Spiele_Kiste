import sys
import pygame
import random
from pygame.math import Vector2

while True:
    pygame.init()
    game_font = pygame.font.Font(None,25)
    cell_size = 25
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            print("update")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("up")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("down")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("right")
    screen.fill((0 ,210 ,30))
    pygame.display.update()
    clock.tick(60)
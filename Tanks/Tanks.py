import pygame
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")

WHITE = (255, 255, 255)
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH//2 - 5 , 0, 10, HEIGHT)

FPS = 60
Bullet = 3
Bulletspeed = 15


Panzer_WIDTH, Panzer_HEIGHT = 100, 60


YELLOW_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


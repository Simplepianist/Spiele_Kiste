import sys
import pygame
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(3,1),Vector2(2,1),Vector2(1,1)]
        self.direction = Vector2(1,0)
        self.new_part = False

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(255,0,0),snake_rect)

    def move_snake(self):
        if self.new_part == True:
            body_copy = self.body[:]
            self.new_part = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_part(self):
        self.new_part = True

class FRUIT:
    def __init__(self):
        self.new_pos()

    def draw_fuit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        #screen.blit(apple,fruit_rect)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def new_pos(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class LOGIK:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0

    def update(self):
        self.snake.move_snake()
        self.can_eat()
        self.is_defeat()

    def draw_elements(self):
        self.fruit.draw_fuit()
        self.snake.draw_snake()

    def can_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_pos()
            self.snake.add_part()
            self.score += 1

    def is_defeat(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.end_game()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.end_game()

    def end_game(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
game = LOGIK()
#apple = pygame.image.load('PATH').convert_alpha()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if game.snake.direction != Vector2(0,1):
                    game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if game.snake.direction != Vector2(0,-1):
                    game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if game.snake.direction != Vector2(1,0):
                    game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if game.snake.direction != Vector2(-1,0):
                    game.snake.direction = Vector2(1,0)
    screen.fill(pygame.Color('gold'))
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)
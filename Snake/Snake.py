import sys
import pygame
import random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(3, 1), Vector2(2, 1), Vector2(1, 1)]
        self.direction = Vector2(1, 0)
        self.new_part = False

        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_rigth.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()

        self.body_hor = pygame.image.load('assets/horizontal.png').convert_alpha()
        self.body_vert = pygame.image.load('assets/vertical.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/bl.png').convert_alpha()

    def draw_snake(self):
        self.select_head()
        self.select_tail()
        for index, block in enumerate(self.body):
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] -block
                next_block = self.body[index - 1] -block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vert,snake_rect)
                elif previous_block.y == next_block.y:
                   screen.blit(self.body_hor, snake_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,snake_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,snake_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,snake_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,snake_rect)


    def select_head(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def select_tail(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_part == True:
            body_copy = self.body[:]
            self.new_part = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_part(self):
        self.new_part = True

class FRUIT:
    def __init__(self):
        self.new_pos()

    def draw_fuit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def new_pos(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class LOGIK:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.defeat = False

    def message(self):
        mesg = pygame.font.SysFont(None,33).render("You Lost! Q for Quiting and R to Play again", True, (255,0,0))
        mes_rec = mesg.get_rect(center = (cell_number * cell_size / 2,cell_number * cell_size / 3))
        scoreend = pygame.font.SysFont(None,33).render("Score was: " + str(len(self.snake.body) - 3), True, (255,0,0))
        screen.blit(mesg, mes_rec)
        scoreend_rec = scoreend.get_rect(center = (cell_number * cell_size / 2,cell_number * cell_size / 2))
        screen.blit(scoreend, scoreend_rec)

    def create_playfield(self):
        grass_color = (167,209,61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)


    def update(self):
        self.snake.move_snake()
        self.can_eat()
        self.is_defeat()

    def draw_elements(self):
        self.create_playfield()
        self.score()
        self.fruit.draw_fuit()
        self.snake.draw_snake()

    def can_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_pos()
            self.snake.add_part()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.new_pos()
    def is_defeat(self):
        self.defeat = False
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.defeat = True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.defeat = True
        if self.defeat:
            screen.fill("blue")
            game.message()
            pygame.display.update()
        return self.defeat


    def score(self):
        score_text = "Score: " + str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_rec = score_surface.get_rect(topleft = (0,0))
        screen.blit(score_surface,score_rec)


    def end_game(self):
        end_font = pygame.font.Font(None,60)
        end_text = "Drücke q um das Spiel zu beenden oder <Enter> zum neustarten"
        end_surface = end_font.render(end_text,True,(56,74,12))
        pos_x = cell_number * cell_size / 2
        pos_y = cell_number * cell_size / 2
        end_rec = end_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(end_surface,end_rec)


pygame.init()
game_font = pygame.font.Font(None,25)
cell_size = 25
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game = LOGIK()
apple = pygame.image.load('assets/fruit.png').convert_alpha()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
while True:
    if game.is_defeat():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    game.__init__()
                    game.draw_elements()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if game.snake.direction != Vector2(0, 1):
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if game.snake.direction != Vector2(0, -1):
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if game.snake.direction != Vector2(1, 0):
                        game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if game.snake.direction != Vector2(-1, 0):
                        game.snake.direction = Vector2(1, 0)
        screen.fill((0,210,30))
        game.draw_elements()
        pygame.display.update()
        clock.tick(60)


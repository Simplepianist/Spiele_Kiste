import sys
import pygame
from random import randint
from pygame.math import Vector2


class BLOCKS:
    def __init__(self):
        self.S = [['.....',
                   '......',
                   '..00..',
                   '.00...',
                   '.....'],
                  ['.....',
                   '..0..',
                   '..00.',
                   '...0.',
                   '.....']]

        self.Z = [['.....',
                   '.....',
                   '.00..',
                   '..00.',
                   '.....'],
                  ['.....',
                   '..0..',
                   '.00..',
                   '.0...',
                   '.....']]

        self.I = [['..0..',
                   '..0..',
                   '..0..',
                   '..0..',
                   '.....'],
                  ['.....',
                   '0000.',
                   '.....',
                   '.....',
                   '.....']]

        self.O = [['.....',
                   '.....',
                   '.00..',
                   '.00..',
                   '.....']]

        self.J = [['.....',
                   '.0...',
                   '.000.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..00.',
                   '..0..',
                   '..0..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.000.',
                   '...0.',
                   '.....'],
                  ['.....',
                   '..0..',
                   '..0..',
                   '.00..',
                   '.....']]

        self.L = [['.....',
                   '...0.',
                   '.000.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..0..',
                   '..0..',
                   '..00.',
                   '.....'],
                  ['.....',
                   '.....',
                   '.000.',
                   '.0...',
                   '.....'],
                  ['.....',
                   '.00..',
                   '..0..',
                   '..0..',
                   '.....']]

        self.T = [['.....',
                   '..0..',
                   '.000.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..0..',
                   '..00.',
                   '..0..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.000.',
                   '..0..',
                   '.....'],
                  ['.....',
                   '..0..',
                   '.00..',
                   '..0..',
                   '.....']]
        self.blocks = [self.S, self.Z, self.I, self.O, self.J, self.L, self.T]

    def generate_block(self):
        select = randint(0, 6)
        self.block = self.blocks[3]


class LOGIK:
    def __init__(self):
        self.player = 0
        self.player1 = False
        self.player2 = False
        self.player3 = False
        self.player4 = False
        self.mode = None
        self.block = BLOCKS()

    def player_settings(self):
        player_font = pygame.font.Font(None, 60)
        player_text = "Choose Player count (1-4)"
        player_surface = player_font.render(player_text, True, (255, 255, 255))
        pos_x = player_x / 2
        pos_y = player_y / 2
        player_rec = player_surface.get_rect(center=(pos_x, pos_y))
        player_settings.blit(player_surface, player_rec)

    def mode_settings(self):
        mode_font = pygame.font.Font(None, 45)
        mode_s_head = 'Type "s" for Survival'
        mode_p_head = 'Type "p" for Points-Mode'
        if self.player > 1:
            mode_s_desc = 'Survive the longest to defeat your Enemys'
            mode_p_desc = 'Get the most Points until the time runs out'
        else:
            mode_s_desc = 'Endless Survival till you die'
            mode_p_desc = 'Farm Points until your timer runs out'

        mode_sh_surface = mode_font.render(mode_s_head, True, (255, 255, 255))
        mode_sd_surface = mode_font.render(mode_s_desc, True, (255, 255, 255))
        mode_ph_surface = mode_font.render(mode_p_head, True, (255, 255, 255))
        mode_pd_surface = mode_font.render(mode_p_desc, True, (255, 255, 255))
        pos_x = mode_x / 2
        pos_y = mode_y / 2
        mode_sd_rect = mode_sd_surface.get_rect(midbottom=(pos_x, pos_y - 50))
        mode_sh_rect = mode_sh_surface.get_rect(midbottom=mode_sd_rect.midtop)
        mode_ph_rect = mode_ph_surface.get_rect(midtop=(pos_x, pos_y + 50))
        mode_pd_rect = mode_pd_surface.get_rect(midtop=mode_ph_rect.midbottom)
        mode_set.blit(mode_ph_surface, mode_ph_rect)
        mode_set.blit(mode_pd_surface, mode_pd_rect)
        mode_set.blit(mode_sh_surface, mode_sh_rect)
        mode_set.blit(mode_sd_surface, mode_sd_rect)

    def create_playfield(self):
        if self.player == 1:
            self.player1 = True
        elif self.player == 2:
            self.player1 = True
            self.player2 = True
        elif self.player == 3:
            self.player1 = True
            self.player2 = True
            self.player3 = True
        else:
            self.player1 = True
            self.player2 = True
            self.player3 = True
            self.player4 = True
        width = border_width / 2
        height = border_height / 2
        full_width_field = field_cell_width * cell_size
        full_height_field = field_cell_height * cell_size
        control_hight = height + full_height_field
        control_width = width + full_width_field / 2
        if self.player == 1 or self.player == 2:
            up_1 = pygame.font.SysFont(None, 33).render("w", True, (255, 255, 255))
            down_1 = pygame.font.SysFont(None, 33).render("s", True, (255, 255, 255))
            left_1 = pygame.font.SysFont(None, 33).render("a", True, (255, 255, 255))
            right_1 = pygame.font.SysFont(None, 33).render("d", True, (255, 255, 255))
            up_2 = pygame.font.SysFont(None, 33).render("^", True, (255, 255, 255))
            down_2 = pygame.font.SysFont(None, 33).render("v", True, (255, 255, 255))
            left_2 = pygame.font.SysFont(None, 33).render("<", True, (255, 255, 255))
            right_2 = pygame.font.SysFont(None, 33).render(">", True, (255, 255, 255))
            control1_up_rect = pygame.Rect(control_width - 15, control_hight, 30, 30)
            control1_down_rect = pygame.Rect(control_width - 15, control_hight + 30, 30, 30)
            control1_left_rect = pygame.Rect(control_width - 45, control_hight + 30, 30, 30)
            control1_right_rect = pygame.Rect(control_width + 15, control_hight + 30, 30, 30)
            control2_up_rect = pygame.Rect(2.8 * control_width - 15, control_hight, 30, 30)
            control2_down_rect = pygame.Rect(2.8 * control_width - 15, control_hight + 30, 30, 30)
            control2_left_rect = pygame.Rect(2.8 * control_width - 45, control_hight + 30, 30, 30)
            control2_right_rect = pygame.Rect(2.8 * control_width + 15, control_hight + 30, 30, 30)
        else:
            up_1 = pygame.font.SysFont(None, 33).render("w", True, (255, 255, 255))
            down_1 = pygame.font.SysFont(None, 33).render("s", True, (255, 255, 255))
            left_1 = pygame.font.SysFont(None, 33).render("a", True, (255, 255, 255))
            right_1 = pygame.font.SysFont(None, 33).render("d", True, (255, 255, 255))
            up_2 = pygame.font.SysFont(None, 33).render("i", True, (255, 255, 255))
            down_2 = pygame.font.SysFont(None, 33).render("k", True, (255, 255, 255))
            left_2 = pygame.font.SysFont(None, 33).render("j", True, (255, 255, 255))
            right_2 = pygame.font.SysFont(None, 33).render("l", True, (255, 255, 255))
            up_3 = pygame.font.SysFont(None, 33).render("^", True, (255, 255, 255))
            down_3 = pygame.font.SysFont(None, 33).render("v", True, (255, 255, 255))
            left_3 = pygame.font.SysFont(None, 33).render("<", True, (255, 255, 255))
            right_3 = pygame.font.SysFont(None, 33).render(">", True, (255, 255, 255))
            up_4 = pygame.font.SysFont(None, 33).render("N8", True, (255, 255, 255))
            down_4 = pygame.font.SysFont(None, 33).render("N5", True, (255, 255, 255))
            left_4 = pygame.font.SysFont(None, 33).render("N4", True, (255, 255, 255))
            right_4 = pygame.font.SysFont(None, 33).render("N6", True, (255, 255, 255))
            control1_up_rect = pygame.Rect(control_width - 15, control_hight, 30, 30)
            control1_down_rect = pygame.Rect(control_width - 15, control_hight + 30, 30, 30)
            control1_left_rect = pygame.Rect(control_width - 45, control_hight + 30, 30, 30)
            control1_right_rect = pygame.Rect(control_width + 15, control_hight + 30, 30, 30)
            control2_up_rect = pygame.Rect(2.8 * control_width - 15, control_hight, 30, 30)
            control2_down_rect = pygame.Rect(2.8 * control_width - 15, control_hight + 30, 30, 30)
            control2_left_rect = pygame.Rect(2.8 * control_width - 45, control_hight + 30, 30, 30)
            control2_right_rect = pygame.Rect(2.8 * control_width + 15, control_hight + 30, 30, 30)
            control3_up_rect = pygame.Rect(4.5 * control_width - 15, control_hight, 30, 30)
            control3_down_rect = pygame.Rect(4.5 * control_width - 15, control_hight + 30, 30, 30)
            control3_left_rect = pygame.Rect(4.5 * control_width - 45, control_hight + 30, 30, 30)
            control3_right_rect = pygame.Rect(4.5 * control_width + 15, control_hight + 30, 30, 30)
            control4_up_rect = pygame.Rect(6.2 * control_width - 15, control_hight, 30, 30)
            control4_down_rect = pygame.Rect(6.2 * control_width - 15, control_hight + 30, 30, 30)
            control4_left_rect = pygame.Rect(6.2 * control_width - 45, control_hight + 30, 30, 30)
            control4_right_rect = pygame.Rect(6.2 * control_width + 15, control_hight + 30, 30, 30)

        if self.player == 1:
            game_rect = pygame.Rect(width, height, full_width_field, full_height_field)
            pygame.draw.rect(screen, (0, 0, 0), game_rect)
            screen.blit(up_1, control1_up_rect)
            screen.blit(down_1, control1_down_rect)
            screen.blit(left_1, control1_left_rect)
            screen.blit(right_1, control1_right_rect)
        elif self.player == 2:
            game1_rect = pygame.Rect(width, height, full_width_field, full_height_field)
            game2_rect = pygame.Rect(2 * width + full_width_field, height, full_width_field, full_height_field)
            pygame.draw.rect(screen, (0, 0, 0), game1_rect)
            pygame.draw.rect(screen, (0, 0, 0), game2_rect)
            screen.blit(up_1, control1_up_rect)
            screen.blit(down_1, control1_down_rect)
            screen.blit(left_1, control1_left_rect)
            screen.blit(right_1, control1_right_rect)
            screen.blit(up_2, control2_up_rect)
            screen.blit(down_2, control2_down_rect)
            screen.blit(left_2, control2_left_rect)
            screen.blit(right_2, control2_right_rect)
        elif self.player == 3:
            game1_rect = pygame.Rect(width, height, full_width_field, full_height_field)
            game2_rect = pygame.Rect(2 * width + full_width_field, height, full_width_field, full_height_field)
            game3_rect = pygame.Rect(3 * width + full_width_field * 2, height, full_width_field, full_height_field)
            pygame.draw.rect(screen, (0, 0, 0), game1_rect)
            pygame.draw.rect(screen, (0, 0, 0), game2_rect)
            pygame.draw.rect(screen, (0, 0, 0), game3_rect)
            screen.blit(up_1, control1_up_rect)
            screen.blit(down_1, control1_down_rect)
            screen.blit(left_1, control1_left_rect)
            screen.blit(right_1, control1_right_rect)
            screen.blit(up_2, control2_up_rect)
            screen.blit(down_2, control2_down_rect)
            screen.blit(left_2, control2_left_rect)
            screen.blit(right_2, control2_right_rect)
            screen.blit(up_3, control3_up_rect)
            screen.blit(down_3, control3_down_rect)
            screen.blit(left_3, control3_left_rect)
            screen.blit(right_3, control3_right_rect)
        elif self.player == 4:
            game1_rect = pygame.Rect(width, height, full_width_field, full_height_field)
            game2_rect = pygame.Rect(2 * width + full_width_field, height, full_width_field, full_height_field)
            game3_rect = pygame.Rect(3 * width + full_width_field * 2, height, full_width_field, full_height_field)
            game4_rect = pygame.Rect(4 * width + full_width_field * 3, height, full_width_field, full_height_field)
            pygame.draw.rect(screen, (0, 0, 0), game1_rect)
            pygame.draw.rect(screen, (0, 0, 0), game2_rect)
            pygame.draw.rect(screen, (0, 0, 0), game3_rect)
            pygame.draw.rect(screen, (0, 0, 0), game4_rect)
            screen.blit(up_1, control1_up_rect)
            screen.blit(down_1, control1_down_rect)
            screen.blit(left_1, control1_left_rect)
            screen.blit(right_1, control1_right_rect)
            screen.blit(up_2, control2_up_rect)
            screen.blit(down_2, control2_down_rect)
            screen.blit(left_2, control2_left_rect)
            screen.blit(right_2, control2_right_rect)
            screen.blit(up_3, control3_up_rect)
            screen.blit(down_3, control3_down_rect)
            screen.blit(left_3, control3_left_rect)
            screen.blit(right_3, control3_right_rect)
            screen.blit(up_4, control4_up_rect)
            screen.blit(down_4, control4_down_rect)
            screen.blit(left_4, control4_left_rect)
            screen.blit(right_4, control4_right_rect)

    def calc_right_width(self):
        if self.player == 2:
            return 0.75
        elif self.player == 3:
            return 0.667
        elif self.player == 4:
            return 0.625

    def player_movement(self, player, move):
        if player == 1:
            if self.player1:
                if move == "UP":
                    print("Player 1 Up")
                elif move == "DOWN":
                    pygame.time.set_timer(UPDATE_PLAYER1, 100)
                elif move == "RIGHT":
                    print("Player 1 RIGHT")
                elif move == "LEFT":
                    print("Player 1 LEFT")
                elif move == "RELEASE":
                    pygame.time.set_timer(UPDATE_PLAYER1, 150)
        elif player == 2:
            if self.player2:
                if move == "UP":
                    print("Player 2 Up")
                elif move == "DOWN":
                    pygame.time.set_timer(UPDATE_PLAYER1, 100)
                elif move == "RIGHT":
                    print("Player 2 RIGHT")
                elif move == "LEFT":
                    print("Player 2 LEFT")
                elif move == "RELEASE":
                    pygame.time.set_timer(UPDATE_PLAYER1, 150)
        elif player == 3:
            if self.player3:
                if move == "UP":
                    print("Player 3 Up")
                elif move == "DOWN":
                    pygame.time.set_timer(UPDATE_PLAYER1, 100)
                elif move == "RIGHT":
                    print("Player 3 RIGHT")
                elif move == "LEFT":
                    print("Player 3 LEFT")
                elif move == "RELEASE":
                    pygame.time.set_timer(UPDATE_PLAYER1, 150)
        elif player == 4:
            if self.player4:
                if move == "UP":
                    print("Player 4 Up")
                elif move == "DOWN":
                    pygame.time.set_timer(UPDATE_PLAYER1, 100)
                elif move == "RIGHT":
                    print("Player 4 RIGHT")
                elif move == "LEFT":
                    print("Player 4 LEFT")
                elif move == "RELEASE":
                    pygame.time.set_timer(UPDATE_PLAYER1, 150)

    def update_field(self, field):
        if field == 1:
            if self.player1:
                print("Update 1")
        elif field == 2:
            if self.player2:
                print("Update 2")
        elif field == 3:
            if self.player3:
                print("")
        elif field == 4:
            if self.player4:
                print("")


pygame.init()
game_font = pygame.font.Font(None, 25)
game = LOGIK()
player_x = 600
player_y = 600
player_settings = pygame.display.set_mode((player_x, player_y))
clock = pygame.time.Clock()
player = False
while not player:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                game.player = 1
                player = True
            if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                game.player = 2
                player = True
            if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                game.player = 3
                player = True
            if event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                game.player = 4
                player = True
    player_settings.fill((0, 0, 0))
    game.player_settings()
    pygame.display.update()
    clock.tick(60)
mode_x = 800
mode_y = 500
mode_set = pygame.display.set_mode((mode_x, mode_y))
mode = False
while not mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game.mode = "Survival"
                mode = True
            if event.key == pygame.K_p:
                game.mode = "Points"
                mode = True
    player_settings.fill((0, 0, 0))
    game.mode_settings()
    pygame.display.update()
    clock.tick(60)
pygame.init()
cell_size = 25
field_cell_width = 10
field_cell_height = 15
UPDATE_PLAYER1 = pygame.USEREVENT
pygame.time.set_timer(UPDATE_PLAYER1, 150)
if game.player == 1:
    border_height = 200
    border_width = 150
    screen = pygame.display.set_mode(
        (border_width + field_cell_width * cell_size, field_cell_height * cell_size + border_height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == UPDATE_PLAYER1:
                game.update_field(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    game.player_movement(1, "UP")
                if event.key == pygame.K_s:
                    game.player_movement(1, "DOWN")
                if event.key == pygame.K_a:
                    game.player_movement(1, "LEFT")
                if event.key == pygame.K_d:
                    game.player_movement(1, "RIGHT")
        screen.fill((1, 125, 26))
        game.create_playfield()
        pygame.display.update()
        clock.tick(60)
else:
    UPDATE_PLAYER2 = pygame.USEREVENT
    pygame.time.set_timer(UPDATE_PLAYER2, 150)
    UPDATE_PLAYER3 = pygame.USEREVENT
    pygame.time.set_timer(UPDATE_PLAYER3, 150)
    UPDATE_PLAYER4 = pygame.USEREVENT
    pygame.time.set_timer(UPDATE_PLAYER4, 150)
    border_height = 200
    border_width = 100
    screen = pygame.display.set_mode((
                                     border_width * game.player * game.calc_right_width() + field_cell_width * cell_size * game.player,
                                     (field_cell_height * cell_size + border_height)))
    game.create_playfield()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == UPDATE_PLAYER1:
                game.update_field(1)
            if event.type == UPDATE_PLAYER2:
                game.update_field(2)
            if event.type == UPDATE_PLAYER3:
                game.update_field(3)
            if event.type == UPDATE_PLAYER4:
                game.update_field(4)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    game.player_movement(1, "RELEASE")
                if event.key == pygame.K_DOWN:
                    if game.player == 2:
                        game.player_movement(2, "RELEASE")
                    else:
                        game.player_movement(3, "RELEASE")
                if event.key == pygame.K_k:
                    if game.player != 2:
                        game.player_movement(2, "RELEASE")
                    else:
                        game.player_movement(3, "RELEASE")
                if event.key == pygame.K_KP_5:
                    game.player_movement(4, "RELEASE")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    game.player_movement(1, "UP")
                if event.key == pygame.K_s:
                    game.player_movement(1, "DOWN")
                if event.key == pygame.K_a:
                    game.player_movement(1, "LEFT")
                if event.key == pygame.K_d:
                    game.player_movement(1, "RIGHT")
                if event.key == pygame.K_UP:
                    if game.player == 2:
                        game.player_movement(2, "UP")
                    else:
                        game.player_movement(3, "UP")
                if event.key == pygame.K_DOWN:
                    if game.player == 2:
                        game.player_movement(2, "DOWN")
                    else:
                        game.player_movement(3, "DOWN")
                if event.key == pygame.K_LEFT:
                    if game.player == 2:
                        game.player_movement(2, "LEFT")
                    else:
                        game.player_movement(3, "LEFT")
                if event.key == pygame.K_RIGHT:
                    if game.player == 2:
                        game.player_movement(2, "RIGHT")
                    else:
                        game.player_movement(3, "RIGHT")
                if event.key == pygame.K_i:
                    if game.player != 2:
                        game.player_movement(2, "UP")
                    else:
                        game.player_movement(3, "UP")
                if event.key == pygame.K_k:
                    if game.player != 2:
                        game.player_movement(2, "DOWN")
                    else:
                        game.player_movement(3, "DOWN")
                if event.key == pygame.K_j:
                    if game.player != 2:
                        game.player_movement(2, "LEFT")
                    else:
                        game.player_movement(3, "LEFT")
                if event.key == pygame.K_l:
                    if game.player != 2:
                        game.player_movement(2, "RIGHT")
                    else:
                        game.player_movement(3, "RIGHT")
                if event.key == pygame.K_KP_8:
                    game.player_movement(4, "UP")
                if event.key == pygame.K_KP_5:
                    game.player_movement(4, "DOWN")
                if event.key == pygame.K_KP_4:
                    game.player_movement(4, "LEFT")
                if event.key == pygame.K_KP_6:
                    game.player_movement(4, "RIGHT")
        screen.fill((1, 125, 26))
        game.create_playfield()
        pygame.display.update()
        clock.tick(60)

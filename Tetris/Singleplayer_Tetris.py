import sys

import pygame
import random

colors = [
    (0, 0, 0),
    (153, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 153),
    (255, 128, 0),
    (153,0,153),
    (255, 255, 153),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):

        self.x = x
        self.y = y
        element = random.randint(0, len(self.figures) - 1)
        self.type = element
        self.color = element + 1
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        self.sound = True
        try:
            self.breakline = pygame.mixer.Sound('assets/break.wav')
            self.end = pygame.mixer.Sound('assets/end.wav')
            self.endplaying = False
            pygame.mixer.music.load('assets/music.mp3')
            pygame.mixer.music.play(-1)
        except:
            self.sound = False

        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):

        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                if self.sound:
                    pygame.mixer.music.pause()
                    self.breakline.play()
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
                if self.sound:
                    pygame.mixer.music.unpause()
        self.score += lines ** 2


    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

    def end_message(self):
        if not self.endplaying:
            if self.sound:
                self.endplaying = True
                pygame.mixer.music.stop()
                self.end.play()
        screen.fill("red")
        mesg1 = pygame.font.SysFont(None, 33).render("You Lost! Q for Quiting", True,
                                                    WHITE)
        mesg2 = pygame.font.SysFont(None, 33).render("      R to Play again", True,
                                                     WHITE)

        mes_rec = mesg1.get_rect(center=( 400/ 2, 500 / 4))
        mes2_rec = mesg1.get_rect(center=(400 / 2, 500 / 3))
        scoreend = pygame.font.SysFont(None, 33).render("Score was: " + str(self.score), True,
                                                        WHITE)
        screen.blit(mesg1, mes_rec)
        screen.blit(mesg2,mes2_rec)
        scoreend_rec = scoreend.get_rect(center=( 400/ 2,500 / 2))
        screen.blit(scoreend, scoreend_rec)


# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
fig = Figure(20,10)

counter = 0

pressing_down = False

while not done:
    if game.state == "gameover":
        game.end_message()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.__init__(20,10)
                    pressing_down = False
                if event.key == pygame.K_q:
                    done = True
    else:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    while pause:
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                pause = False
                                done = True
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_ESCAPE:
                                    pause = False


        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        screen.fill((0,102,0))

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, BLACK, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom])

                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(screen, colors[game.figure.color],
                                         [game.x + game.zoom * (j + game.figure.x) + 1,
                                          game.y + game.zoom * (i + game.figure.y) + 1,
                                          game.zoom - 2, game.zoom - 2])


    # font = pygame.font.SysFont('Calibri', 25, True, False)
    # font1 = pygame.font.SysFont('Calibri', 65, True, False)
    # text = font.render("Score: " + str(game.score), True, BLACK)
    # text_game_over = font1.render("Game Over", True, (255, 125, 0))
    # text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    # screen.blit(text, [0, 0])
    # if game.state == "gameover":
    #     screen.blit(text_game_over, [20, 200])
    #     screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
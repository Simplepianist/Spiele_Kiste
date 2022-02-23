import pygame

class WORDLIST:
    def __init__(self):
        self.wordlist = []

    def fill(self, count):
        if count == 5:
            folder = 'assets/wordlist_5.txt'
        else:
            folder = 'assets/wordlist_6.txt'
        with open(folder) as f:
            for line in f:
                self.wordlist.append(line.replace("\n","").strip())

class GAME:
    def __init__(self):
        self.playing = True
        self.setting = False

    def player_settings(self):
        player_font = pygame.font.Font(None, 60)
        player_text = "5 oder 6 Buchstaben"
        player_surface = player_font.render(player_text, True, (255, 255, 255))
        pos_x = 500 / 2
        pos_y = 500 / 3
        player_rec = player_surface.get_rect(center=(pos_x, pos_y))
        settings.blit(player_surface, player_rec)

pygame.init()
game = GAME()
settings = pygame.display.set_mode((500,500))
setting_done = False
while game.playing:
    if not game.setting:
        #game.player_settings()
        settings.fill("green")

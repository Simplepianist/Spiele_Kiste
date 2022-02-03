import pygame

#Parameter
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
FPS = 60





pygame.display.set_caption("Hangman")

def draw_window():
    
    pygame.display.update()

def main():
    draw_window
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

if __name__ == "__main__":
    main()
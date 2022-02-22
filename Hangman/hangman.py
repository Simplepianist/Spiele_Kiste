import pygame


pygame.init()

window = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Hangman")

#Farben
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

font = pygame.font.Font("freesansbold.ttf", 40)
text = font.render("Hangman", True, black)

textRect = text.get_rect()
textRect.center = (640 // 2, 30)

#Bilder einfügen
pfahl = pygame.image.load('Assets/Pfahl.png')
seil = pygame.image.load('Assets/Seil.png')
koerper = pygame.image.load('Assets/Körper.png')
kopf = pygame.image.load('Assets/Kopf.png')
beine = pygame.image.load('Assets/Beine.png')
arme = pygame.image.load('Assets/Arme.png')


while True:
    window.fill(white)

    window.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()

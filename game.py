import pygame
from materials.Player import Player

pygame.init()

BG = pygame.color.THECOLORS['lightblue']
gameScreen = pygame.display.set_mode((640, 380))
pygame.display.set_caption('Samoloty')

clock = pygame.time.Clock()

exitGame = False

player = Player()

while not exitGame:
    gameScreen.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        player.listenEvents(event)

    player.draw(gameScreen)
    player.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

import pygame
from pygame.locals import *
from materials.Player import Player
from state.Window import Window
from levels.Level import Level


pygame.init()
pygame.display.set_caption('Samoloty')
BG = pygame.color.THECOLORS['lightblue']
window = Window()

clock = pygame.time.Clock()
exitGame = False

player = Player()
currentLevel = Level()
player.level = currentLevel

while not exitGame:
    window.getScreen().fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        player.listenEvents(event)


    currentLevel.draw(window.getScreen())
    player.draw(window.getScreen())
    player.update(window.getDimension())
    currentLevel.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

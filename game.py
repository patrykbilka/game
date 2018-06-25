import pygame
from pygame.locals import *
from materials.Player import Player
from state.Window import WIDTH, HEIGHT
from levels.Level import Level


# pygame.init()
# pygame.display.set_caption('Samoloty')
# window = Window()
#
# clock = pygame.time.Clock()
# exitGame = False

player = Player()
currentLevel = Level(player)
player.level = currentLevel
class Game(object):
    def __init__(self):
        self.tps_max = 100.0
        pygame.init()
        BG = pygame.color.THECOLORS['lightblue']
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                player.listenKeyboard(event)

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            self.screen.fill(BG)
            self.draw()
            pygame.display.flip()
    def tick(self):
        player.update(WIDTH, HEIGHT)
        currentLevel.update()

    def draw(self):
        player.draw(self.screen)
        currentLevel.draw(self.screen)


Game()

pygame.quit()
quit()

import pygame
from pygame.locals import *
from materials.Player import Player
from state.static import WIDTH, HEIGHT
from levels.Level import Level

class Game(object):
    def __init__(self):
        pygame.init()
        BG = pygame.color.THECOLORS['lightblue']
        self.fps_max = 120.0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = Player()
        self.currentLevel = Level(self.player)
        self.player.level = self.currentLevel
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                self.player.listenKeyboard(event)

            self.fps_delta += self.fps_clock.tick() / 1000.0
            while self.fps_delta > 1 / self.fps_max:
                self.tick()
                self.fps_delta -= 1 / self.fps_max

            self.screen.fill(BG)
            self.draw()
            pygame.display.flip()
    def tick(self):
        self.player.update(WIDTH, HEIGHT)
        self.currentLevel.update()

    def draw(self):
        self.player.draw(self.screen)
        self.currentLevel.draw(self.screen)


Game()

pygame.quit()
quit()

import pygame

WIDTH = 640
HEIGHT = 480

class Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dimensionX = WIDTH
        self.dimensionY = HEIGHT
        self.screen = pygame.display.set_mode((self.dimensionX, self.dimensionY))

    def getScreen(self):
        return self.screen

    def getDimension(self):
        return (self.dimensionX, self.dimensionY)

    def getDimensionX(self):
        return self.dimensionX

    def getDimensionY(self):
        return self.dimensionY

import os, pygame
from materials.Enemy import Enemy

class Level:
    def __init__(self):
        self.start = pygame.time.get_ticks()
        self.current = pygame.time.get_ticks()
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.world_shift = 0

    def draw(self, surface):
        self.missiles.draw(surface)
        self.enemies.draw(surface)

    def update(self):
        self.current = pygame.time.get_ticks()
        seconds = (self.current - self.start)/1000
        if seconds > 5.0:
            enemy = Enemy()
            self.enemies.add(enemy)
            self.start = pygame.time.get_ticks()

        self.missiles.update()
        self.enemies.update()
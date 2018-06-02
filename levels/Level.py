import os, pygame
from materials.Enemy import Enemy

class Level:
    def __init__(self):
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        for i in range(5):
            enemy = Enemy()
            print(enemy.rect)
            self.enemies.add(enemy)
        self.world_shift = 0

    def draw(self, surface):
        self.missiles.draw(surface)
        self.enemies.draw(surface)

    def update(self):
        self.missiles.update()
        self.enemies.update()

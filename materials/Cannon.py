import os, pygame, random
from static.resolution import WIDTH, HEIGHT
from materials.CannonBullet import CannonBullet
image = pygame.image.load(os.path.join('assets', 'cannon.png'))

class Cannon(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.start = pygame.time.get_ticks()
        self.current = pygame.time.get_ticks()
        self.level = level
        self.image = image
        self.rect = self.image.get_rect()
        self.width = 38
        self.height = 38
        self.rect.y = HEIGHT - self.height
        self.rect.x = WIDTH
        self.speed = 1

    def update(self):
        self.rect.x -= self.speed

        self.current = pygame.time.get_ticks()
        seconds = (self.current - self.start)/1000
        if seconds > 3.0:
            bullet = CannonBullet()
            bullet.rect.y = self.rect.y + 30
            bullet.rect.x = self.rect.x + 10
            self.level.cannonBullets.add(bullet)
            self.start = pygame.time.get_ticks()

        if (self.rect.x + self.width) <= 0:
            self.kill()

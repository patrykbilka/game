import os, pygame
from static.resolution import WIDTH, HEIGHT

image = pygame.image.load(os.path.join('assets', 'cannon_bullet.png'))

class CannonBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

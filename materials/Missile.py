import os, pygame
from static.resolution import WIDTH, HEIGHT

image = pygame.image.load(os.path.join('assets', 'missile.png'))

class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 15

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH - self.rect.width:
            self.kill()

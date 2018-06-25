import os, pygame, random
from state.static import WIDTH, HEIGHT
image = pygame.image.load(os.path.join('assets', 'cannon.png'))

class Cannon(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
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
        if (self.rect.x + self.width) <= 0:
            self.kill()

import os, pygame
from state.static import WIDTH, HEIGHT

image = pygame.image.load(os.path.join('assets', 'bomb.png'))

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT - self.rect.height:
            self.kill()

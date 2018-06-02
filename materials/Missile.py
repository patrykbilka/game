import os, pygame

image = pygame.image.load(os.path.join('assets', 'missile.png'))

class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 25

    def update(self):
        self.rect.x += self.speed
        

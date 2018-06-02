import os, pygame, random
from state.Window import WIDTH, HEIGHT
image = pygame.image.load(os.path.join('assets', 'enemy.png'))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.width = 150
        self.height = 70
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.rect.x = random.randrange(WIDTH + 40, WIDTH + 300)
        self.speed = 0.3

    def update(self):
        self.rect.x -= self.speed
        if (self.rect.x + self.rect.width) < 0:
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.rect.x = random.randrange(WIDTH + 40, WIDTH + 100)

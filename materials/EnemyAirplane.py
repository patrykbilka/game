import os, pygame, random
from static.resolution import WIDTH, HEIGHT
image = pygame.image.load(os.path.join('assets', 'enemy.png'))

class EnemyAirplane(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.image = image
        self.rect = self.image.get_rect()
        self.width = 150
        self.height = 40
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height - 120)
        self.rect.x = WIDTH
        self.speed = random.randrange(3, 8)

    def update(self):
        self.rect.x -= self.speed
        if (self.rect.x + self.rect.width) < 0:
            self.kill()

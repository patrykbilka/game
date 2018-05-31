import os, pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'samolot.png'))
        self.rect = self.image.get_rect()
        self.directionY = 0

    def draw(self, surface):
        print(self.rect)
        surface.blit(self.image, self.rect)

    def turnUp(self):
        self.directionY = -3

    def turnDown(self):
        self.directionY = 3

    def stop(self):
        self.directionY = 0

    def update(self):
        self.rect.y += self.directionY

    def listenEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.turnUp()
            elif event.key == pygame.K_s:
                self.turnDown()
        if event.type == pygame.KEYUP:
            self.stop()

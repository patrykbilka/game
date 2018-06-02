import os, pygame
from materials.Missile import Missile

image = pygame.image.load(os.path.join('assets', 'plane2.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.level = None
        self.width = 90
        self.height = 50
        self.directionY = 1
        self.directionX = 0
        self.speed = 4
        self.idleSpeed = 1
        self.imageStartingPoint = 50

    def draw(self, surface):
        surface.blit(self.image, self.rect, (0, self.imageStartingPoint, self.width, self.height))

    def turnUp(self):
        self.directionY = -self.speed
        self.changeAnimationType(0)

    def turnDown(self):
        self.directionY = self.speed
        self.changeAnimationType(100)

    def turnLeft(self):
        self.directionX = -(self.speed / 2)
        self.changeAnimationType(50)

    def turnRight(self):
        self.directionX = (self.speed / 2)
        self.changeAnimationType(50)

    def stop(self, value = 0):
        self.directionY = value
        self.changeAnimationType(50)

    def update(self, screenSize):
        if self.rect.y + self.directionY < screenSize[1] - self.height - 50 and self.rect.y + self.directionY > 0:
            self.rect.y += self.directionY
        if self.rect.x + self.directionX < screenSize[0] - self.width and self.rect.x + self.directionX > 0:
            self.rect.x += self.directionX

    def changeAnimationType(self, startingPoint):
        self.imageStartingPoint = startingPoint

    #shoot
    def shotMissile(self):
        missile = Missile()
        print(self.rect)
        missile.rect.y = self.rect.y + (self.height / 2) + 5
        missile.rect.x = self.rect.x + self.rect.width + 5
        self.level.missiles.add(missile)

    def listenEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turnUp()
            elif event.key == pygame.K_DOWN:
                self.turnDown()
            elif event.key == pygame.K_LEFT:
                self.turnLeft()
            elif event.key == pygame.K_RIGHT:
                self.turnRight()
            elif event.key == pygame.K_SPACE:
                self.shotMissile()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.stop(-(self.idleSpeed))
            elif event.key == pygame.K_DOWN:
                self.stop(self.idleSpeed)

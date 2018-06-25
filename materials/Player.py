import os, pygame
from pygame.math import Vector2
from state.Window import WIDTH, HEIGHT
from materials.Missile import Missile

image = pygame.image.load(os.path.join('assets', 'plane2.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.level = None
        self.width = 90
        self.height = 50

        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.idleSpeed = 5
        self.directionY = 0
        self.directionX = 0
        self.acceleration = 1
        self.imageStartingPoint = 50

    def addForce(self, force):
        self.acc += force

    def update(self, width, height):

        self.listenKeyboard()
        self.vel *= 0.97777777777777777777777777777
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        # Boundries

        if self.pos.x + self.width > WIDTH:
            self.vel = Vector2(0, 0)
            self.pos.x = WIDTH - self.width
        if self.pos.x < 0:
            self.vel = Vector2(0, 0)
            self.pos.x = 0
        if self.pos.y + self.height > HEIGHT:
            self.vel = Vector2(0, 0)
            self.pos.y = HEIGHT - self.height
        if self.pos.y < 0:
            self.vel = Vector2(0, 0)
            self.pos.y = 0

    def draw(self, surface):
        surface.blit(self.image, self.pos, (0, self.imageStartingPoint, self.width, self.height))

    def turnUp(self):
        self.directionY = -self.acceleration
        self.changeAnimationType(0)

    def turnDown(self):
        self.directionY = self.acceleration
        self.changeAnimationType(100)

    def turnLeft(self):
        self.directionX = -self.acceleration

    def turnRight(self):
        self.directionX = self.acceleration
        self.acceleration *= 1.1

    def resetAnimation(self):
        self.changeAnimationType(50)

    def stopMovementX(self, value = 0):
        self.directionX = 0

    def stopMovementY(self, value = 0):
        self.directionY = 0

    def changeAnimationType(self, startingPoint):
        self.imageStartingPoint = startingPoint

    #shoot
    def shotMissile(self):
        missile = Missile()
        missile.rect.y = self.rect.y + (self.height / 2) + 5
        missile.rect.x = self.rect.x + self.rect.width + 5
        self.level.missiles.add(missile)

    def listenKeyboard(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.addForce(Vector2(0, -0.5))
            self.changeAnimationType(0)
        elif pressed[pygame.K_DOWN]:
            self.addForce(Vector2(0, 0.5))
            self.changeAnimationType(100)
        elif pressed[pygame.K_LEFT]:
            self.addForce(Vector2(-0.5, 0))
            self.resetAnimation()
        elif pressed[pygame.K_RIGHT]:
            self.addForce(Vector2(0.5, 0))
            self.resetAnimation()
        else:
            self.resetAnimation()

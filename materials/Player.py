import os, pygame
from pygame.math import Vector2
from state.static import WIDTH, HEIGHT
from materials.Missile import Missile
from materials.Bomb import Bomb

image = pygame.image.load(os.path.join('assets', 'player.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.height = 50
        self.levelocity = None
        self.width = 148
        self.height = 50

        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.imageStartingPoint = 50

    def addForce(self, speed):
        self.acceleration += speed

    def kill(self):
        pygame.quit()

    def update(self, width, height):
        self.handleMovement()
        self.velocity *= 0.988
        self.velocity += self.acceleration
        self.position += self.velocity
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.acceleration *= 0

        # Boundries
        if self.position.x + self.width > WIDTH:
            self.velocity = Vector2(0, 0)
            self.position.x = WIDTH - self.width
        if self.position.x < 0:
            self.velocity = Vector2(0, 0)
            self.position.x = 0
        if self.position.y + self.height > HEIGHT:
            self.velocity = Vector2(0, 0)
            self.position.y = HEIGHT - self.height
        if self.position.y < 0:
            self.velocity = Vector2(0, 0)
            self.position.y = 0

    def draw(self, surface):
        surface.blit(self.image, self.position, (0, self.imageStartingPoint, self.width, self.height))

    def resetAnimation(self):
        self.changeAnimationType(50)

    def changeAnimationType(self, startingPoint):
        self.imageStartingPoint = startingPoint

    #shoot
    def shotMissile(self):
        missile = Missile()
        missile.rect.y = self.position.y + (self.height / 2) + 5
        missile.rect.x = self.position.x + self.width + 5
        self.level.missiles.add(missile)
    #shoot
    def shotBomb(self):
        bomb = Bomb()
        bomb.rect.y = self.position.y + (self.height / 2) + 5
        bomb.rect.x = self.position.x + (self.width / 2) - bomb.rect.width / 2
        self.level.bombs.add(bomb)

    def handleMovement(self):
        speed = 0.3
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.addForce(Vector2(0, -speed))
            self.changeAnimationType(0)
        elif pressed[pygame.K_DOWN]:
            self.addForce(Vector2(0, speed))
            self.changeAnimationType(100)
        elif pressed[pygame.K_LEFT]:
            self.addForce(Vector2(-speed, 0))
            self.resetAnimation()
        elif pressed[pygame.K_RIGHT]:
            self.addForce(Vector2(speed, 0))
            self.resetAnimation()
        else:
            self.resetAnimation()

    def listenKeyboard(self, event):
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
             self.shotMissile()

         if event.key == pygame.K_r:
             self.shotBomb()

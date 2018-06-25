import os, pygame
from materials.EnemyAirplane import EnemyAirplane
from materials.Cannon import Cannon

class Level:
    def __init__(self, player):
        self.player = player
        self.start = pygame.time.get_ticks()
        self.initStart = pygame.time.get_ticks()
        self.current = pygame.time.get_ticks()
        self.missiles = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cannons = pygame.sprite.Group()
        self.world_shift = 0

    def draw(self, surface):
        self.missiles.draw(surface)
        self.enemies.draw(surface)
        self.cannons.draw(surface)
        self.bombs.draw(surface)

    def update(self):
        missilesAirplanesCollisions = pygame.sprite.groupcollide(
            self.enemies, self.missiles, True, True)


        bombsCannonsCollisions = pygame.sprite.groupcollide(
            self.cannons, self.bombs, True, True)

        playerHits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if playerHits:
            self.player.kill()

        self.current = pygame.time.get_ticks()
        seconds = (self.current - self.start)/1000
        secondsToSpawn = (self.current - self.initStart)/1000
        if seconds > 1.5:
            enemy = EnemyAirplane(self)
            self.enemies.add(enemy)
            enemy = EnemyAirplane(self)
            self.enemies.add(enemy)
            self.start = pygame.time.get_ticks()

        if secondsToSpawn > 5.0:
            cannon = Cannon(self)
            self.cannons.add(cannon)
            self.initStart = pygame.time.get_ticks()

        self.missiles.update()
        self.enemies.update()
        self.cannons.update()
        self.bombs.update()

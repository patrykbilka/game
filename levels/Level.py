import os, pygame
from materials.EnemyAirplane import EnemyAirplane

class Level:
    def __init__(self, player):
        self.player = player
        self.start = pygame.time.get_ticks()
        self.current = pygame.time.get_ticks()
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.world_shift = 0

    def draw(self, surface):
        self.missiles.draw(surface)
        self.enemies.draw(surface)

    def update(self):
        colliding_platforms = pygame.sprite.groupcollide(
            self.enemies, self.missiles, True, True)

        playerHits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if playerHits:
            self.player.kill()

        self.current = pygame.time.get_ticks()
        seconds = (self.current - self.start)/1000
        if seconds > 1.0:
            enemy = EnemyAirplane(self)
            self.enemies.add(enemy)
            enemy = EnemyAirplane(self)
            self.enemies.add(enemy)
            self.start = pygame.time.get_ticks()

        self.missiles.update()
        self.enemies.update()

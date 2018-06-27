import os, pygame
from materials.EnemyAirplane import EnemyAirplane
from materials.Cannon import Cannon
from static.resolution import WIDTH, HEIGHT

bg = pygame.image.load(os.path.join('assets', 'bg_game.jpg'))
bg_finish = pygame.image.load(os.path.join('assets', 'bg.jpg'))
ground = pygame.image.load(os.path.join('assets', 'ground.png'))
class Level:
    def __init__(self, player, started, screen, game):
        self.game = game
        self.player = player
        self.started = started
        self.screen = screen
        self.playerLives = True
        self.start = pygame.time.get_ticks()
        self.initStart = pygame.time.get_ticks()
        self.current = pygame.time.get_ticks()
        self.missiles = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cannons = pygame.sprite.Group()
        self.cannonBullets = pygame.sprite.Group()
        self.world_shift = 0

    def draw(self):
        points = str(self.player.points)
        title = self.formatText(points, 30, (0, 0, 0))
        self.screen.blit(bg, (0, 0))
        self.screen.blit(ground, (0, HEIGHT - 50))
        self.screen.blit(title, [20, 20])
        self.missiles.draw(self.screen)
        self.enemies.draw(self.screen)
        self.cannons.draw(self.screen)
        self.bombs.draw(self.screen)
        self.cannonBullets.draw(self.screen)

    def update(self):

        if self.player.points >= 100:
            self.player.win = True
            # self.displayWin()

        missilesAirplanesCollisions = pygame.sprite.groupcollide(
            self.enemies, self.missiles, True, True)

        if missilesAirplanesCollisions:
            self.player.points += 5

        bombsCannonsCollisions = pygame.sprite.groupcollide(
            self.cannons, self.bombs, True, True)

        if bombsCannonsCollisions:
            self.player.points += 15

        playerAirplaneHits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if playerAirplaneHits:
            self.player.lost = True
            # self.displayLost()

        playerCannonBulletsHits = pygame.sprite.spritecollide(self.player, self.cannonBullets, False)
        if playerCannonBulletsHits:
            self.player.lost = True
            # self.displayLost()

        self.current = pygame.time.get_ticks()
        seconds = (self.current - self.start)/1000
        secondsToSpawn = (self.current - self.initStart)/1000
        if seconds > 1.5:
            enemy = EnemyAirplane(self)
            self.enemies.add(enemy)
            # enemy = EnemyAirplane(self)
            # self.enemies.add(enemy)
            self.start = pygame.time.get_ticks()

        if secondsToSpawn > 5.0:
            cannon = Cannon(self)
            self.cannons.add(cannon)
            self.initStart = pygame.time.get_ticks()

        self.missiles.update()
        self.enemies.update()
        self.cannons.update()
        self.bombs.update()
        self.cannonBullets.update()

    def formatText(self, message, size, color):
        textFont = "font.ttf"
        newFont=pygame.font.Font(textFont, size)
        newText=newFont.render(message, 0, color)
        return newText

    def displayWin(self):
        points = str(self.player.points)
        title = self.formatText("Przeszedłeś level! punkty: " + str(points), 50, (255, 255, 255))
        self.screen.blit(bg_finish, (0, 0))
        self.screen.blit(title, [WIDTH / 2, HEIGHT / 2])

    def displayLost(self):
        points = str(self.player.points)
        title = self.formatText("Zostałeś zestrzelony! punkty: " + str(points), 50, (255, 255, 255))
        self.screen.blit(bg_finish, (0, 0))
        self.screen.blit(title, [WIDTH / 2, HEIGHT / 2])

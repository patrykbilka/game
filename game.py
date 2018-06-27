import os, pygame
from pygame.locals import *
from materials.Player import Player
from static.resolution import WIDTH, HEIGHT
from levels.Level import Level
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

bg_finish = pygame.image.load(os.path.join('assets', 'bg.jpg'))
class Game(object):
    def __init__(self):
        pygame.init()
        self.fps_max = 120.0
        self.mainMenu = True
        self.gamePaused = False
        self.bg = pygame.image.load(os.path.join('assets', 'bg.jpg'))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = Player()
        self.currentLevel = Level(self.player, self.mainMenu, self.screen, self)
        self.player.level = self.currentLevel
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0
        if self.mainMenu:
            self.menu(self.screen)

        self.initLoop()

    def initLoop(self):
        while not self.player.lost and not self.player.win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.player.listenKeyboard(event)

            self.fps_delta += self.fps_clock.tick() / 1000.0
            while self.fps_delta > 1 / self.fps_max:
                self.tick()
                self.fps_delta -= 1 / self.fps_max

            self.screen.fill(blue)
            self.draw()
            pygame.display.flip()
        if self.player.win:
            self.displayWin()
        elif self.player.lost:
            self.displayLost()

    def tick(self):
        self.player.update()
        self.currentLevel.update()

    def draw(self):
        self.currentLevel.draw()
        self.player.draw(self.screen)

    def formatText(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    def menu(self, screen):
        selected="start"
        fontTitle = "3rd Man.ttf"
        font = "font.ttf"

        while self.mainMenu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            self.mainMenu = False
                        if selected=="quit":
                            pygame.quit()
                            exit()

            screen.fill(blue)
            title=self.formatText("WWII shooter", fontTitle, 120, (100, 123, 100))
            if selected=="start":
                text_start=self.formatText("Start", font, 50, (100, 123, 100))
            else:
                text_start = self.formatText("Start", font, 50, black)
            if selected=="quit":
                text_quit=self.formatText("exit", font, 50, (100, 123, 100))
            else:
                text_quit = self.formatText("exit", font, 50, black)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
            screen.blit(self.bg, (0, 0))
            screen.blit(title, (WIDTH - (title_rect.width + 50), HEIGHT - 250))
            screen.blit(text_start, (WIDTH/3 - (start_rect[2]/2), 220))
            screen.blit(text_quit, (WIDTH/3 - (quit_rect[2]/2), 260))
            pygame.display.update()
            pygame.display.set_caption("World War II shooter")

    def displayWin(self):
        pygame.display.update()
        font = "font.ttf"
        points = str(self.player.points)
        title = self.formatText("Przeszedłeś level! punkty: " + str(points), font, 50, (255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill(blue)
            self.screen.blit(bg_finish, (0, 0))
            self.screen.blit(title, [WIDTH / 2, HEIGHT / 2])
            pygame.display.update()

    def displayLost(self):
        font = "font.ttf"
        points = str(self.player.points)
        title = self.formatText("Zostałeś zestrzelony! punkty: " + str(points), font, 50, (255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill(blue)
            self.screen.blit(bg_finish, (0, 0))
            self.screen.blit(title, [WIDTH / 2, HEIGHT / 2])
            pygame.display.update()

Game()

pygame.quit()
exit()

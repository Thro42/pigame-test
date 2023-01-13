from random import randint
import pygame
import pygame.math
import sys
from Config import *

import Player
import Bullet
import Enemy


class Game:
    bullets = []
    enemys = []

    def __init__(self, breite: int, hoehe: int):
        self.game_over = False
        self.youWin = False 
        self.player = None
        size = (breite, hoehe)
        self.fenster = pygame.display.set_mode(size, pygame.RESIZABLE)
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        for n in range(4):
            pos = pygame.math.Vector2(randint(10, 700), 20)
            enemy = Enemy.Enemy(self, pos)
            self.enemys.append(enemy)

    def initPlayer(self):
        # Init the Player
        p_pos = pygame.math.Vector2(400, 580)
        p_size = pygame.math.Vector2(40, 40)
        
        self.player = Player.Player(self, "space-ship.png", p_pos, p_size)
        self.player.enableCenter(True)

    def SetPlayer(self, player: Player):
        self.player = player

    def AddBullet(self, bullet: Bullet):
        # einen Kugel merken
        self.bullets.append(bullet)

    def FireBullet(self, pos: pygame.math.Vector2):
        if len(self.bullets) <= 6:
            # Kugel Instanzieren
            bullet = Bullet.Bullet(self, pos)
            # die Kugel merken
            self.bullets.append(bullet)

    def KillBullet(self, bullet: Bullet):
        # Kugel beseitigen
        self.bullets.remove(bullet)

    def KillEnemy(self, enemy: Enemy):
        # Feind beseitigen
        self.enemys.remove(enemy)

    def CheckHit(self, bullet: Bullet):
        # Prüfen üb die Kugel einen Treffer hat
        bpos = bullet.position
        for enemy in self.enemys:
            epos = enemy.position
            if ((bpos.y <= (epos.y + enemy.size.y/2)            # ist die Kugel schon über dem Feind
                 and ((bpos.x > (epos.x - enemy.size.x/2))      # Kugel links im Feind
                 and (bpos.x < (epos.x + enemy.size.x/2))))):   # Kugel rechts im Feind
                enemy.Hit(bullet)

    def HandleKeybord(self):
        # Tastatur befele verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                if event.key == pygame.K_q:
                    self.game_over = True
                if event.key == pygame.K_RIGHT:
                    self.player.dx = 4
                elif event.key == pygame.K_LEFT:
                    self.player.dx = -4
                elif event.key == pygame.K_SPACE:
                    self.player.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.dx = 0
                elif event.key == pygame.K_RIGHT:
                    self.player.dx = 0

    def showEnd(self):
        self.gameover = pygame.image.load("game_over.png")
        self.gameover = pygame.transform.scale(self.gameover, (self.fenster.get_width(), self.fenster.get_height()))
        self.youwinImg = pygame.image.load("youwin.png")
        self.youwinImg = pygame.transform.scale(self.youwinImg, (self.fenster.get_width(), self.fenster.get_height()))
        imgrec = pygame.Rect(0, 0, self.fenster.get_width(), self.fenster.get_height())
        if self.youWin:
            self.fenster.blit(self.youwinImg, imgrec)
        else:
            self.fenster.blit(self.gameover, imgrec)

    def loop(self):
        # -------- Main Program Loop -----------
        while not self.game_over:
            # --- Main event loop
            self.HandleKeybord()
            self.fenster.fill(GRAY)
            self.player.loop()
            # Schleife für die Kugeln
            for bullet in self.bullets:
                bullet.loop()
            # Schleife für die Feinden
            for enemy in self.enemys:
                enemy.loop()
            if len(self.enemys) <= 0:
                self.youWin = True
                self.game_over = True
            pygame.display.update()
            self.clock.tick(60)
        # Ende Zeigen
        while True:
            self.fenster.fill(GRAY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                    if event.key == pygame.K_q:
                        sys.exit()
            self.showEnd()
            pygame.display.update()
            self.clock.tick(60)
            


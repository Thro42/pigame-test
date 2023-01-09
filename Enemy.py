from random import randint
import pygame
import pygame.math
from Config import *
import Game
import Bullet


class Enemy:
    def __init__(self, game: Game, pos: pygame.math.Vector2):
        self.game = game
        self.live = True
        self.has_hit = False
        self.position = pygame.math.Vector2(pos.x, pos.y)
        self.size = pygame.math.Vector2(40, 40)
        self.image = pygame.image.load("alien-ship.png")
        self.esplow = pygame.image.load("explo.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.speed = -3
        self.rec = pygame.Rect(pos.x - (self.size.x /2), pos.y - (self.size.y /2 ) , self.size.x, self.size.y)

    def Hit(self, bullet: Bullet):
        # Feind ist getroffen
        self.size = pygame.math.Vector2(40, 40)
        self.has_hit = True
        self.image = pygame.transform.scale(self.esplow, self.size)

    def explore_loop(self):
        # Schleife für Explosion
        self.size.x += 2
        self.size.y += 2
        self.image = pygame.transform.scale(self.esplow, self.size)
        if self.size.x > 100:
            self.game.KillEnemy(self)

    def loop(self):
        if not self.has_hit:
            move_x = randint(-3, 3)
            self.position.x += move_x
        else:
            self.explore_loop()
        pos = self.position
        self.rec = pygame.Rect(pos.x - (self.size.x /2), pos.y - (self.size.y /2 ) , self.size.x, self.size.y)
        self.game.fenster.blit(self.image, self.rec)

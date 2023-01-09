import pygame
import pygame.math
from Config import *
import Game


class Bullet:
    def __init__(self, game: Game, pos: pygame.math.Vector2) -> None:
        self.game = game
        self.life = True
        self.position = pygame.math.Vector2(pos.x, pos.y)
        self.size = pygame.math.Vector2(12, 25)
        self.image = pygame.image.load("Fire.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.speed = -3
        self.rec = pygame.Rect(pos.x - (self.size.x /2), pos.y - (self.size.y /2 ) , self.size.x, self.size.y)

    def loop(self):
        if self.position.y >= 0:
            self.position.y += self.speed
            pos = self.position
            self.rec = pygame.Rect(pos.x - (self.size.x /2), pos.y - (self.size.y /2 ) , self.size.x, self.size.y)
            self.game.fenster.blit(self.image, self.rec)
            # Schauen wir mal ob wir was getroffen haben
            self.game.CheckHit(self)
        else:
            # Kugel ist ausserhalb des Spielfeldes
            self.game.KillBullet(self)



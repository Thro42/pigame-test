import pygame
import pygame.math
from Config import *
import Game
import Bullet


class Player:
    def __init__(self, game: Game, img: str, pos: pygame.math.Vector2, size: pygame.math.Vector2):
        self.game = game
        self.life = True
        self.draw_center = False
        self.dx = 0
        self.posistion = pos
        self.size = size
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, size)
        self.player = pygame.Rect(pos.x - (size.x/2), pos.y - (size.y/2), size.x, size.y)

    def enableCenter(self, state: bool):
        self.draw_center = state

    def set_pos(self, pos: pygame.math.Vector2):
        self.posistion = pos
        self.player = pygame.Rect(pos.x - (self.size.x /2), pos.y - (self.size.y /2 ) , self.size.x, self.size.y)

    def move_x(self):
        pos = self.posistion
        pos.x = pos.x + self.dx
        pos.y = self.game.fenster.get_height() - self.size.y/2
        self.set_pos(pos)

    def draw(self):
        self.game.fenster.blit(self.image, self.player)

    def loop(self):
        self.draw()
        self.move_x()

    def fire(self):
        pos = pygame.math.Vector2(self.posistion.x, self.posistion.y)
        pos.y = pos.y - self.size.y/2
        bullet = Bullet.Bullet(self.game, pos)
        self.game.AddBullet(bullet)

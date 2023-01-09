import pygame
import pygame.math
from Config import *
# import Game
from Game import Game

# PYGame Initialisieren
pygame.init()
# Grösse festlegen
game = Game(800, 600)
# Spieler initialisieren
game.initPlayer()
# Start Loop
game.loop()

# Close the window and quit.
pygame.quit()

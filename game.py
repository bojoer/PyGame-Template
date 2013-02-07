import sys
import math
import pygame
import random
import constants

from pygame.locals import *
from models.game import Game
from utils.misc import logger

log = logger(__name__)

def main():
    while 1:
        pygame.init()
        log.info('Starting game %s', constants.CAPTION)
        game = Game()
        game.begin()

if __name__ == "__main__":
        main()

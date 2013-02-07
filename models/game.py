import sys
import pygame
import constants

from models.map import Map
from pygame.locals import *
from utils.misc import logger
from models.player import Player

log = logger(__name__)

class Game(object):
    def __init__(self):

        self.player = Player()
        self.clock = pygame.time.Clock()
        self.map = Map()
#        self.map.setPlayer(self.player)
#        self.screen.draw_screen_layers(player_stats=self.player_stats, map=self.map)
        
        screen=pygame.display.set_mode([constants.SIZE_WIDTH, constants.SIZE_HEIGHT])
        pygame.display.set_caption(constants.CAPTION)
        log.info('Map setup')
        
    def begin(self):
        log.info('Begin game')
        self.run()
        
    def refreshScreen(self):
        pygame.display.flip()
#        self.screen.draw_player(self.map.player)
#        self.screen.draw_screen_layers(self.map, self.player_stats)

    def endGame(self):
        log.info('End called')
        sys.exit()

    def run(self):
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.endGame()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        self.endGame()
            self.refreshScreen()
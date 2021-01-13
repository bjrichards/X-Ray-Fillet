# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame
from .Entity import Player, Platform


# Class
class EntityMgr():
    def __init__(self, engine):
        self.engine = engine

        pass

    
    def initialize(self):

        self.player = Player(self.engine, None, (40, 40), 0, self.engine.gfxMgr.window)
        self.player.initialize()

        self.platforms = []

        platform = Platform(self.engine, None, (400, 30), 0, self.engine.gfxMgr.window, (0, 600))
        self.platforms.append(platform)
        platform = Platform(self.engine, None, (400, 30), 0, self.engine.gfxMgr.window, (1024-400, 300))
        self.platforms.append(platform)


    def tick(self, dt):
        self.player.tick(dt)


    def shutdown(self):
        pass
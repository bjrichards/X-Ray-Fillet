# Created by Braeden Richards
# Created on January 7th, 2021
# Desc:


# Includes
import pygame
from .Button import Button


# Class
class UiMgr():
    def __init__(self, engine):
        self.engine = engine

        self.in_game = None
        self.show_fps = None

    
    def initialize(self):
        self.in_game = False
        self.show_fps = self.engine.config.show_fps


    def tick(self, dt):
        if self.show_fps:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_fps(), (10, 0))
        self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_is_grounded(), (300, 0))
        self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_double_jump(), (600, 0))


    def shutdown(self):
        pass
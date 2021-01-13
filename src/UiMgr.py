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
        self.show_grounded = None
        self.show_jumps_left = None
        self.show_bullet_count = None

    
    def initialize(self):
        self.in_game = False
        self.show_fps = self.engine.config.show_fps
        self.show_grounded = self.engine.config.show_is_grounded
        self.show_jumps_left = self.engine.config.show_jumps_left
        self.show_bullet_count = self.engine.config.show_bullet_count


    def tick(self, dt):
        if self.show_fps:
            self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_fps(), (10, 0))
        if self.show_grounded:
            self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_is_grounded(), (200, 0))
        if self.show_jumps_left:
            self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_show_jumps(), (400, 0))
        if self.show_bullet_count:
            self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_bullet_count(), (600, 0))


    def shutdown(self):
        pass
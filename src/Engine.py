# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
from sys import exit
from pygame import time
from .GfxMgr import GfxMgr
from .UiMgr import UiMgr
from .EntityMgr import EntityMgr
from .GameMgr import GameMgr
from .InputMgr import InputMgr


# Class
class Engine():
    def __init__(self, config_class):
        self.config = config_class

        self.gfxMgr = GfxMgr(self)
        self.uiMgr = UiMgr(self)
        self.entityMgr = EntityMgr(self)
        self.gameMgr = GameMgr(self)
        self.inputMgr = InputMgr(self)

        self.fps = self.config.fps

        self.keepRunning = True

        self.clock = time.Clock()
        self.gravity = 0

    def initialize(self):
        self.gfxMgr.initialize(self.config.window_name, self.config.window_size)
        self.uiMgr.initialize()
        self.gameMgr.initialize()
        self.entityMgr.initialize()

        
        self.inputMgr.initialize()


    def tick_all(self):
        dt = self.clock.tick(self.fps)

        self.gfxMgr.tick(dt)
        self.uiMgr.tick(dt)
        self.entityMgr.tick(dt)
        self.gameMgr.tick(dt)
        self.inputMgr.tick()


    def run(self):
        while self.keepRunning == True:
            self.tick_all()


    def cleanup(self):
        self.gfxMgr.shutdown()
        exit()  # sys.exit
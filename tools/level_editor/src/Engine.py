# Created by Braeden Richards
# Created on August 5th, 2021

# IMPORTS #

from src.EntityMgr import EntityMgr
from src.AppMgr import AppMgr
from src.GfxMgr import GfxMgr
from src.InputMgr import InputMgr
from sys import exit
from pygame import time
from json import dumps

# Class
class Engine():
    def __init__(self, config_class, map_file):
        self.config = config_class
        self.map_file = map_file

        self.gfx_mgr = GfxMgr(self)
        self.entity_mgr = EntityMgr(self)
        self.app_mgr = AppMgr(self)
        self.input_mgr = InputMgr(self)

        self.fps = self.config.fps
        self.keep_running = True

        self.clock = time.Clock()


    def initialize(self):
        self.gfx_mgr.initialize(self.config.window_name, self.config.window_size)
        self.entity_mgr.initialize()
        self.app_mgr.initialize()
        self.input_mgr.initialize()


    def tick_all(self):
        dt = self.clock.tick(self.fps)

        self.gfx_mgr.tick(dt)
        self.app_mgr.tick(dt)
        self.input_mgr.tick(dt)


    def run(self):
        while self.keep_running == True:
            self.tick_all()


    def clean_up(self):
        self.save_file()
        exit()  # sys.exit

    def save_file(self):
        # create dict
        temp_dict = {}
        for sprite in self.entity_mgr.layer_0_placed_sprites:
            temp_dict[sprite.identity] = [sprite.entity_type, sprite.position]
        # jsonify
        fo = open('data/maps/' + self.map_file, "w")
        fo.write(dumps(temp_dict))
        fo.close()
  
        
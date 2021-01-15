# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame


# Class
class GameMgr():
    def __init__(self, engine):
        self.engine = engine

        self.platforms = []

        self.game_status = None

        self.player_load_pos = None
        

    
    def initialize(self):
        self.game_status = 'MENU'

    def load_level(self, level):
        self.engine.gravity = 0
        self.create_active_map()
        self.engine.entityMgr.load_map()
        self.engine.gfxMgr.scroll[0] = self.engine.entityMgr.furthest_object 
        self.engine.entityMgr.player.position =  self.player_load_pos

        self.game_status = 'IN_GAME'
        self.engine.gravity = self.engine.config.gravity


    def tick(self, dt):
        if self.game_status == 'START':
            self.load_level(1)


    def shutdown(self):
        pass

    def create_active_map(self):
        self.platforms = []
        self.enemies = []
        
        row = 0
        col = 0
        width = 0
        start = 0
        active = False

        self.f = open("data\map.txt", 'r')
        print(self.f.read())
        self.f.close()
        self.f = open("data\map.txt", 'r')
        while 1:
            char = self.f.read(1)
            if not char:
                if active == True:
                    platform = (start, width * (1024 / 12), row * (768 / 9))
                    self.platforms.append(platform)
                break
            if (char == '\n'):
                if active == True:
                        platform = (start, width * (1024 / 12), row * (768 / 9))
                        self.platforms.append(platform)
                active = False
                row = row + 1
                col = 0
                width = 0
            else:
                if char == '=':
                    if active == False:
                        active = True
                        start = col * (1024 / 12)
                    width = width + 1    
                else:
                    if active == True:
                        platform = (start, width * (1024 / 12), row * (768 / 9))
                        self.platforms.append(platform)
                    if char == '0':
                        start = col * (1024 / 12)
                        enemy = (start, row * (768 / 9))
                        self.enemies.append(enemy)
                    elif char == 'X':
                        start = col * (1024 / 12)
                        self.player_load_pos = (start, row * (768 / 9))
                    width = 0
                    active = False
                col = col + 1
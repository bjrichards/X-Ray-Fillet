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
        

    
    def initialize(self):
        self.create_active_map()
        self.engine.entityMgr.load_map()


    def tick(self, dt):
        pass


    def shutdown(self):
        pass

    def create_active_map(self):
        self.platforms = []

        row = 0
        col = 0
        width = 0
        start = 0
        active = False

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
                    active = False
                col = col + 1
        print(self.platforms)
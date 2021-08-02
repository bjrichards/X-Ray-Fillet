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
        self.player_lives = 10
        self.goal = None
        
        self.current_level = 0
        self.max_level = 3
    
    def initialize(self):
        self.game_status = 'MENU'

    def load_level(self, level):

        self.clean_values_on_load()

        self.engine.gravity = 0

        self.create_active_map(level)
        self.engine.entityMgr.load_map()
        
        self.engine.gfxMgr.scroll[0] = self.goal[0]
        self.engine.gfxMgr.scroll[1] = self.goal[1]

        self.game_status = 'ENTRY_ANIMATION'
        self.engine.gravity = self.engine.config.gravity

        self.current_level = level

    def tick(self, dt):
        if self.game_status == 'MENU':
            pass
        elif self.game_status == 'START':
            self.load_level(1)
        elif self.player_lives == 0:
            self.load_level(self.current_level)
        elif len(self.engine.entityMgr.enemies) == 0:
            if self.current_level + 1 <= self.max_level:
                self.load_level(self.current_level + 1)
            else:
                self.game_status = 'MENU'
                self.current_level = 0


    def shutdown(self):
        pass


    def clean_values_on_load(self):
        # Clean Player values
        self.player_lives = 10
        self.engine.entityMgr.player.moving_left = False
        self.engine.entityMgr.player.moving_right = False

        # Set scroll animation to go on
        self.engine.gfxMgr.scroll_locked = False


    def create_active_map(self, level):
        self.platforms = []
        self.enemies = []

        scale = (32, 32)

        nmap = []
        
        row = 0
        col = 0

        self.f = open("data\map" + str(level) + ".txt", 'r')
        for line in self.f.read().split('\n'):
            nmap.append(line)
        self.f.close()

        self.player_load_pos = (0, 0)

        for line in nmap:
            col = 0
            for char in line:                
                # Check for Platform
                if char == 'G':
                    platform = (col * scale[0], row * scale[1], 'G')
                    self.platforms.append(platform)
                elif char == 'D':
                    platform = (col * scale[0], row * scale[1], 'D')
                    self.platforms.append(platform)
                elif char == 'I':
                    platform = (col * scale[0], row * scale[1], 'I')
                    self.platforms.append(platform)
                elif char == 'L':
                    platform = (col * scale[0], row * scale[1], 'L')
                    self.platforms.append(platform)
                elif char == 'l':
                    platform = (col * scale[0], row * scale[1], 'l')
                    self.platforms.append(platform)
                elif char == 'B':
                    platform = (col * scale[0], row * scale[1], 'B')
                    self.platforms.append(platform)
                elif char == 'R':
                    platform = (col * scale[0], row * scale[1], 'R')
                    self.platforms.append(platform)
                elif char == 'r':
                    platform = (col * scale[0], row * scale[1], 'r')
                    self.platforms.append(platform)
                elif char == 'E':
                    platform = (col * scale[0], row * scale[1], 'E')
                    self.platforms.append(platform)
                elif char == 'X':
                    self.player_load_pos = (col * scale[0], row * scale[1])

                elif char == '0':
                    enemy = (col * scale[0], row * scale[1])
                    self.enemies.append(enemy)
                
                elif char == '?':
                    self.goal = (col * scale[0], row * scale[1])

                col += 1
            row += 1
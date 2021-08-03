# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame
from .Entity import Player, Platform, Enemy


# Class
class EntityMgr():
    def __init__(self, engine):
        self.engine = engine

        pass

    
    def initialize(self):

        self.player = Player(self.engine, self.engine.config.image_file_character_stand, (8, 27), 0, self.engine.gfxMgr.window, (0,0), (32, 32))
        self.player.initialize()

        self.platforms = []
        self.furthest_object = 0

        self.particles = []

        self.enemies = []
        
        self.bullets = []

    def load_map(self):
        self.platforms = []
        self.furthest_object = 0

        self.particles = []

        self.enemies = []
        
        self.bullets = []
        for platform in self.engine.gameMgr.platforms:
            if platform[2] == 'G':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_top_mid)
                pType = 'G'
            elif platform[2] == 'D':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_edge)
                pType = 'D'
            elif platform[2] == 'L':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_top_left)
                pType = 'L'
            elif platform[2] == 'l':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_bottom_left)
                pType = 'l'
            elif platform[2] == 'B':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_bottom_mid)
                pType = 'B'
            elif platform[2] == 'R':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_top_right)
                pType = 'R'
            elif platform[2] == 'r':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_bottom_right)
                pType = 'r'
            elif platform[2] == 'E':
                image = self.engine.gameMgr.spritesheet.get_image(*self.engine.config.platform_bottom_mid_mid)
                pType = 'E'
            elif platform[2] == 'I':
                image = None
                pType = 'I'
            scale = self.engine.config.scale
            newPlatform = Platform(self.engine, image, (32, 32), 0, self.engine.gfxMgr.window, (platform[0] * scale, platform[1] * scale), pType)

            self.platforms.append(newPlatform)

        for enemy in self.engine.gameMgr.enemies:
            newEnemy = Enemy(self.engine, self.engine.config.image_file_enemy_0, (16, 32), len(self.enemies), self.engine.gfxMgr.window)
            newEnemy.position = (enemy[0] * scale, enemy[1] * scale)
            self.enemies.append(newEnemy)

        self.player.load_level((self.engine.gameMgr.player_load_pos[0] * scale, self.engine.gameMgr.player_load_pos[1] * scale))

    
    def tick(self, dt):
        if self.engine.gameMgr.game_status == 'IN_GAME':
            self.player.tick(dt)

            for enemy in self.enemies:
                enemy.tick(dt)

            self.bullets[:] = [bullet for bullet in self.bullets if bullet.tick(dt)]

            
            self.particles[:] = [particle for particle in self.particles if particle.tick(dt)]



    def shutdown(self):
        pass
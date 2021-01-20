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

        self.player = Player(self.engine, self.engine.config.image_file_character_0, (16, 32), 0, self.engine.gfxMgr.window, (0,0))
        self.player.initialize()

        self.platforms = []
        self.furthest_object = 0

        self.particles = []

        self.enemies = []
        
        self.bullets = []

    def load_map(self):
        for platform in self.engine.gameMgr.platforms:
            if platform[2] == 'G':
                image = self.engine.config.image_file_grass_0
                pType = 'G'
            elif platform[2] == 'D':
                image = self.engine.config.image_file_dirt_0
                pType = 'D'
            elif platform[2] == 'I':
                image = None
                pType = 'I'
            scale = self.engine.config.scale
            newPlatform = Platform(self.engine, image, (32, 32), 0, self.engine.gfxMgr.window, (platform[0] * scale, platform[1] * scale), pType)

            self.platforms.append(newPlatform)
            if newPlatform.position[0] > self.furthest_object:
                self.furthest_object = newPlatform.position[0]

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

            for bullet in self.bullets:
                bullet.tick(dt)
            
            for particle in self.particles:
                particle.tick(dt)

            self.bullets[:] = [bullet for bullet in self.bullets if bullet.still_alive() and not bullet.check_collision()]
            self.particles[:] = [particle for particle in self.particles if particle.still_alive()]



    def shutdown(self):
        pass
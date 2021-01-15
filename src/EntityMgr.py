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

        self.player = Player(self.engine, None, (40, 40), 0, self.engine.gfxMgr.window)
        self.player.initialize()

        self.platforms = []
        self.furthest_object = 0

        self.enemies = []
        # platform = Platform(self.engine, None, (400, 30), 0, self.engine.gfxMgr.window, (0, 600))
        
        # platform = Platform(self.engine, None, (400, 30), 0, self.engine.gfxMgr.window, (1024-400, 300))
        # self.platforms.append(platform)

        self.bullets = []

    def load_map(self):
        for platform in self.engine.gameMgr.platforms:
            newPlatform = Platform(self.engine, None, (platform[1], 30), 0, self.engine.gfxMgr.window, (platform[0], platform[2]))
            self.platforms.append(newPlatform)
            if newPlatform.position[0] > self.furthest_object:
                self.furthest_object = newPlatform.position[0]

        for enemy in self.engine.gameMgr.enemies:
            newEnemy = Enemy(self.engine, None, (30, 60), len(self.enemies), self.engine.gfxMgr.window)
            newEnemy.position = (enemy[0], enemy[1])
            self.enemies.append(newEnemy)

    def tick(self, dt):
        if self.engine.gameMgr.game_status == 'IN_GAME':
            self.player.tick(dt)

            for enemy in self.enemies:
                enemy.tick(dt)

            for bullet in self.bullets:
                bullet.tick(dt)

            self.bullets[:] = [bullet for bullet in self.bullets if bullet.still_alive() and not bullet.check_collision()]


    def shutdown(self):
        pass
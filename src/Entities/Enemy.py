# IMPORTS #

# Libraries #
from pygame import Rect, image, transform
from math import sqrt
from random import randrange

# Custom Imports #
from ..Aspects.Physics2D import Physics2D

from .Entity import Entity

from .Bullet import Bullet


class Enemy (Entity):
    def __init__(self, engine, image_file_name, size, identity, display):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Enemy"
        
        self.color = (255, 0, 0)
        self.bullet_color = self.engine.config.enemy_bullet_color
        self.rect = Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
        self.image_file_path = image_file_name
        self.image = image.load(self.image_file_path).convert()        
        self.image = transform.scale(self.image, self.size)

        self.aspects.append(Physics2D(self))

        self.is_grounded = False

        self.max_velocity = (0.3, 1.5)

        self.single_jumped = False
        self.double_jumped = False
        self.jump = 0

        self.moving_left = False
        self.moving_right = False
        self.down_button = False

        self.bullet_speed = self.engine.config.enemy_bullet_speed

    def tick(self, dt):
        
        if self.in_camera():
            if self.engine.entityMgr.player.position[0] + 100 < self.position[0]:
                self.moving_right = False
                self.moving_left = True
            elif self.engine.entityMgr.player.position[0] - 100 > self.position[0]:
                self.moving_right = True
                self.moving_left = False
            else:
                self.moving_right = False
                self.moving_left = False
            
            for aspect in self.aspects:
                aspect.tick(dt)
            
            self.check_enemy_collisions()

            if self.engine.config.enemies_can_fire and self.in_camera():
                if randrange(1, 100, 1) > 98:
                    self.fire(self.engine.entityMgr.player.position)
            # posx = self.position[0] + self.velocity[0] * dt
            # posy = self.position[1] + self.velocity[1] * dt

            # self.position = (posx, posy)
            # self.check_collisions()

    def draw(self):
        if self.in_camera():
            scroll = self.engine.gfxMgr.scroll
            position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
            self.display_surface.blit(self.image, position)
            
            if self.engine.config.bounding_boxes:
                self.rect = Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])

            self.engine.gfxMgr.enemies_rendered += 1

    def check_collisions(self):
        self.check_enemy_collisions()
        


    def check_enemy_collisions(self):
        for enemy in self.engine.entityMgr.enemies:
            if self.identity != enemy.identity:
                if self.position[0] + self.size[0] > enemy.position[0] - 10 and self.position[0] < enemy.position[0] + enemy.size[0] + 10:
                    if self.position[1] + self.size[1] > enemy.position[1] and self.position[1] < enemy.position[1] + enemy.size[1]:
                        if self.position[0] < enemy.position[0] + enemy.size[0] / 2:
                            posx = enemy.position[0] - self.size[0] - 10
                            posy = self.position[1]

                            self.position = (posx, posy)
                        else:
                            posx = enemy.position[0] + self.size[0] + 10
                            posy = self.position[1]

                            self.position = (posx, posy)


    def in_camera(self):
        result = False
        
        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfxMgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfxMgr.scroll[1]:
                result = True

        return result


    def fire(self, pos_to_fire_toward):
        distance = [pos_to_fire_toward[0] - self.position[0], pos_to_fire_toward[1] - self.position[1]]
        normalized = sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normalized, distance[1] / normalized]

        velocity = (direction[0] * self.bullet_speed, direction[1] * self.bullet_speed)

        bullet = Bullet(self.engine, None, (3, 3), 0, self.display_surface, (self.position[0], self.position[1]), velocity, "enemy", self.bullet_color)
        self.engine.entityMgr.bullets.append(bullet)

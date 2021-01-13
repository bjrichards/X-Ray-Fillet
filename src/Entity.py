# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame
import math
from .Aspect import Physics2D

# Class
class Entity():
    def __init__(self, engine, image_file_name, size, identity, display):
        self.engine = engine

        self.entity_type = "Entity"
        self.image_file_name = image_file_name

        self.display_surface = display

        self.position = (0,0)
        self.velocity = (0,0)
        self.acceleration = (0,0)

        self.identity = identity
        self.name = str(self.entity_type) + str(self.identity)

        self.size = size
        self.speed = (0,0)
        self.aspects = []

        if self.engine.config.bounding_boxes == True:
            self.bouding_box = True

    
    def initialize(self):
        pass
        # Open file below and make into entity


    def tick(self, dt):
        pass


    def draw(self):
        if self.is_on_screen():
            self.display_surface.blit(self.image, self.position)

            if self.engine.config.bounding_boxes:
                # pygame.draw.rect(self.display_surface, self.color, self.rect, 1)
                pygame.draw.circle(self.display_surface, self.color, (self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2), 20, 1)


    def is_on_screen(self):
        result = True

        if self.position[0] > self.engine.config.window_size[0] or self.position[0] + self.size[0] < 0:
            result = False

        elif self.position[1] > self.engine.config.window_size[1] or self.position[1] + self.size[1] < 0:
            result = False
        
        return result


    def shutdown(self):
        pass


class Player(Entity):
    def __init__(self, engine, image_file_name, size, identity, display):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Player"
        
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
        self.aspects.append(Physics2D(self))

        self.is_grounded = False

        self.max_velocity = (1, 1.5)

        self.single_jumped = False
        self.double_jumped = False
        self.jump = 0

        self.moving_left = False
        self.moving_right = False

        self.bullet_speed = self.engine.config.player_bullet_speed

    def tick(self, dt):
        for aspect in self.aspects:
            aspect.tick(dt)

        posx = self.position[0] + self.velocity[0] * dt
        posy = self.position[1] + self.velocity[1] * dt

        self.position = (posx, posy)
        self.check_collisions()

    def draw(self):
        if self.is_on_screen():
            self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
            # self.display_surface.blit(self.display_surface, self.rect)

            if self.engine.config.bounding_boxes:
                pygame.draw.rect(self.display_surface, self.color, self.rect, 1)
                pygame.draw.circle(self.display_surface, self.color, (self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2), 20, 1)


    def check_collisions(self):
        if self.keep_in_screen():
            self.is_grounded = True
            self.double_jumped = False
            self.jump = 0
        elif self.check_platform_collisions():
            self.is_grounded = True
            self.double_jumped = False
            self.jump = 0
        else:
            self.is_grounded = False

    def keep_in_screen(self):
        collision = False
        if self.position[1] + self.size[1]>= self.engine.config.window_size[1]:
            self.position = (self.position[0], self.engine.config.window_size[1] - self.size[1])
            self.velocity = (self.velocity[0], 0)
            self.double_jumped = False
            self.single_jumped = False

            collision = True

        elif self.position[1] < 0:
            self.position = (self.position[0], 0)
            self.velocity = (self.velocity[0], 0)

        if self.position[0] <= 0:
            self.position = (0, self.position[1])
        if self.position[0] + self.size[0] > self.engine.config.window_size[0]:
            self.position = (self.engine.config.window_size[0] - self.size[0], self.position[1])
        return collision


    def check_platform_collisions(self):
        collision = False
        if self.velocity[1] >= 0:
            for platform in self.engine.entityMgr.platforms:
                if self.position[0] + self.size[0]  >= platform.position[0] and self.position[0] <= platform.position[0] + platform.size[0]:
                    if self.position[1] + self.size[1] >= platform.position[1] and self.position[1] + self.size[1] <= platform.position[1] + platform.size[1]:
                        self.position = (self.position[0], platform.position[1] - self.size[1]+1)

                        collision = True
                        self.is_grounded = True
                        break
        return collision


    def jump_(self):
        velx = self.velocity[0]
        vely = self.velocity[1]
        self.is_grounded = False

        if self.jump < 2:
            self.jump = self.jump + 1
            
            velx = self.velocity[0]
            vely = -1.4
        
        self.velocity = (velx, vely)


    def fire(self, pos_to_fire_toward):
        distance = [pos_to_fire_toward[0] - self.position[0], pos_to_fire_toward[1] - self.position[1]]
        normalized = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normalized, distance[1] / normalized]

        velocity = (direction[0] * self.bullet_speed, direction[1] * self.bullet_speed)

        bullet = Bullet(self.engine, None, (5, 5), 0, self.display_surface, (self.position[0], self.position[1]), velocity)
        self.engine.entityMgr.bullets.append(bullet)

    
class Platform(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = (100, 255, 100)
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        


    def draw(self):
        if self.engine.config.bounding_boxes:
                pygame.draw.rect(self.display_surface, self.color, self.rect)


class Bullet(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, velocity):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = (255, 0, 0)
        self.position = position
        self.velocity = velocity
        self.is_alive = True
        self.time_alive = 0
        self.lifetime_max = self.engine.config.player_bullet_lifetime
    

    def tick(self, dt):
        posx = self.position[0] + self.velocity[0] * dt
        posy = self.position[1] + self.velocity[1] * dt
        self.position = (posx, posy)
        self.time_alive = self.time_alive + self.engine.clock.get_time()
        self.is_alive = self.still_alive()
        

    def draw(self):
        self.circle = pygame.draw.circle(self.display_surface, self.color, (self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2), self.size[0])


    def still_alive(self):
        result = False

        if self.time_alive / 1000 < self.lifetime_max:
            result = True
        
        return result
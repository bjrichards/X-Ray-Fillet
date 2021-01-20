# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame
import math, random
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

        self.size = (size[0] * self.engine.config.scale, size[1] * self.engine.config.scale)
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
    def __init__(self, engine, image_file_name, size, identity, display, position):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Player"
        
        self.color = (255, 255, 255)
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.image_file_path = image_file_name
        self.image = pygame.image.load(self.image_file_path).convert()        
        self.image = pygame.transform.scale(self.image, self.size)

        self.aspects.append(Physics2D(self))

        self.is_grounded = False

        self.max_velocity = (self.engine.config.max_player_vel[0], self.engine.config.max_player_vel[1])

        self.single_jumped = False
        self.double_jumped = False
        self.jump = 0

        self.moving_left = False
        self.moving_right = False
        self.down_button = False

        self.bullet_speed = self.engine.config.player_bullet_speed

    def tick(self, dt):
        for aspect in self.aspects:
            aspect.tick(dt)

    def load_level(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])


    def draw(self):
        scroll = self.engine.gfxMgr.scroll
        position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
        self.display_surface.blit(self.image, position)
        
        if self.engine.config.bounding_boxes:
            self.rect = pygame.Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])


    def check_collisions(self):
        # if self.keep_in_screen():
        #     self.is_grounded = True
        #     self.double_jumped = False
        #     self.jump = 0
        if self.check_platform_collisions():
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

        return collision


    def jump_(self):
        if (self.is_grounded == True and self.jump == 0) or (self.is_grounded == False and self.jump < 2): 
            self.is_grounded = False

            self.jump = self.jump + 1
            
            velx = self.velocity[0]
            vely = -1.5
            
            self.velocity = (velx, vely)


    def fire(self, pos_to_fire_toward):
        distance = [pos_to_fire_toward[0] + self.engine.gfxMgr.scroll[0] - self.position[0], pos_to_fire_toward[1] + self.engine.gfxMgr.scroll[1] - self.position[1]]
        normalized = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normalized, distance[1] / normalized]

        velocity = (direction[0] * self.bullet_speed, direction[1] * self.bullet_speed)

        bullet = Bullet(self.engine, None, (3, 3), 0, self.display_surface, (self.position[0], self.position[1]), velocity)
        self.engine.entityMgr.bullets.append(bullet)

    
class Platform(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = (100, 255, 100)
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.image_file_path = image_file_name
        self.image = pygame.image.load(self.image_file_path).convert()      
        self.size = (self.image.get_size()[0] * self.engine.config.scale, self.image.get_size()[1] * self.engine.config.scale)
        self.image = pygame.transform.scale(self.image, self.size)


    def draw(self):
        if self.in_camera():
            scroll = self.engine.gfxMgr.scroll
            position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
            self.display_surface.blit(self.image, position)

            if self.engine.config.bounding_boxes:
                self.rect = pygame.Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])
                pygame.draw.rect(self.display_surface, self.color, self.rect)
            self.engine.gfxMgr.platforms_rendered += 1


    def in_camera(self):
        result = True
        
        if self.position[0] + self.size[0] < self.engine.gfxMgr.scroll[0] or self.position[0] > self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0]:
            result = False

        if self.position[1] + self.size[1] < self.engine.gfxMgr.scroll[1] or self.position[1] > self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1]:
            result = False

        return result


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
        self.circle = pygame.draw.circle(self.display_surface, self.color, (self.position[0] - self.engine.gfxMgr.scroll[0] + self.size[0] / 2, self.position[1] - self.engine.gfxMgr.scroll[1] + self.size[1] / 2), self.size[0])


    def still_alive(self):
        result = False

        if self.time_alive / 1000 < self.lifetime_max:
            result = True

        if not self.in_camera():
            result = False
        
        return result

    
    def check_collision(self):
        index = 0

        cx = self.position[0] + self.size[0] / 2
        cy = self.position[1] + self.size[1] / 2
        r = self.size[0]

        for enemy in self.engine.entityMgr.enemies:
            rx = enemy.position[0]
            ry = enemy.position[1]
            rw = enemy.size[0]
            rh = enemy.size[1]

            collision = False
            
            testx = cx
            testy = cy

            if cx < rx:
                testx = rx
            elif cx > rx + rw:
                testx = rx + rw
            if cy < ry:
                testy = ry
            elif cy > ry + rh:
                testy = ry + rh

            distx = cx - testx
            disty = cy - testy
            distance = math.sqrt((distx * distx) + (disty * disty))

            if distance <= r:
                collision = True

            if collision == True:
                self.engine.entityMgr.enemies.pop(index)
                self.create_explosive_particles()
                return True

            index = index + 1

    def create_explosive_particles(self):
        number_of_particles = random.randrange(3, 30, 1)

        for i in range(number_of_particles):
            size = random.randrange(1, 2, 1)
            pos = self.position

            velocity_x = random.triangular(-1, 1)
            velocity_y = random.triangular(-1, 1)

            particle = Particle(self.engine, None, (size, size), len(self.engine.entityMgr.particles), self.engine.gfxMgr.window, pos, (velocity_x, velocity_y))
            self.engine.entityMgr.particles.append(particle)


    def in_camera(self):
        result = True
        
        if self.position[0] + self.size[0] < self.engine.gfxMgr.scroll[0] or self.position[0] > self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0]:
            result = False

        return result


class Enemy (Entity):
    def __init__(self, engine, image_file_name, size, identity, display):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Enemy"
        
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
        self.image_file_path = image_file_name
        self.image = pygame.image.load(self.image_file_path).convert()        
        self.image = pygame.transform.scale(self.image, self.size)

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
                self.rect = pygame.Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])

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

        

    def keep_in_screen(self):
        collision = False
        if self.position[1] + self.size[1]>= self.engine.config.window_size[1]:
            self.position = (self.position[0], self.engine.config.window_size[1] - self.size[1])
            self.velocity = (self.velocity[0], 0)
            collision = True

        elif self.position[1] < 0:
            self.position = (self.position[0], 0)
            self.velocity = (self.velocity[0], 0)

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


    def in_camera(self):
        result = True
        
        if self.position[0] + self.size[0] < self.engine.gfxMgr.scroll[0] or self.position[0] > self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0]:
            result = False

        return result


# Particle Entity
class Particle(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, velocity):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Particle"

        self.velocity = velocity

        self.position = position
        
        self.color = (255, 0, 0)
        
        self.time_alive = 0


    def draw(self):
        self.circle = pygame.draw.circle(self.display_surface, self.color, (self.position[0] - self.engine.gfxMgr.scroll[0] + self.size[0] / 2, self.position[1] - self.engine.gfxMgr.scroll[1] + self.size[1] / 2), self.size[0])

    
    def tick(self, dt):
        Entity.tick(self, dt)

        self.time_alive = self.time_alive + self.engine.clock.get_time()
        
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)


    def still_alive(self):
        result = False

        if self.time_alive / 1000 < 5:
            result = True
        
        return result
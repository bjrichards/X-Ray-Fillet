# IMPORTS #

# Libraries #
from pygame import draw
from math import sqrt
from random import randrange, triangular

# Custom Imports #
from .Entity import Entity
from .Particle import Particle

class Bullet(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, velocity, bType, bullet_color):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = bullet_color
        self.position = position
        self.velocity = velocity
        self.is_alive = True
        self.time_alive = 0
        self.lifetime_max = self.engine.config.player_bullet_lifetime
        self.bType = bType
    

    def tick(self, dt):
        posx = self.position[0] + self.velocity[0] * dt
        posy = self.position[1] + self.velocity[1] * dt
        self.position = (posx, posy)
        self.time_alive = self.time_alive + self.engine.clock.get_time()
        self.is_alive = self.still_alive()

        result = self.is_alive
        if result:
            result = not (self.check_collision())
        
        return result

    def draw(self):
        if self.in_camera():
            draw.circle(self.display_surface, self.color, (self.position[0] - self.engine.gfxMgr.scroll[0] + self.size[0] / 2, self.position[1] - self.engine.gfxMgr.scroll[1] + self.size[1] / 2), self.size[0])


    def still_alive(self):
        result = False

        if self.time_alive / 1000 < self.lifetime_max:
            result = True

        for platform in self.engine.entityMgr.platforms:
            if platform.pType != 'I':
                pos = self.position
                size = self.size

                ppos = platform.position
                psize = platform.size

                if pos[0] + size[0] > ppos[0] and pos[0] < ppos[0] + psize[0] and pos[1] + size[1] > ppos[1] and pos[1] < ppos[1] + psize[1]:
                    result = False
                    self.create_explosive_particles()
                    break
        
        return result

    
    def check_collision(self):
        index = 0

        if self.bType == 'player':
            for enemy in self.engine.entityMgr.enemies:
                if self.check_collision_entity(enemy):
                    self.engine.entityMgr.enemies.pop(index)
                    self.create_explosive_particles()
                    return True
                index = index + 1

        elif self.bType == 'enemy':
            if self.check_collision_entity(self.engine.entityMgr.player):
               self.engine.gameMgr.player_lives -= 1
               self.create_explosive_particles() 

               return True

    
    def check_collision_entity(self, entity):
        cx = self.position[0] + self.size[0] / 2
        cy = self.position[1] + self.size[1] / 2
        r = self.size[0]

        rx = entity.position[0]
        ry = entity.position[1]
        rw = entity.size[0]
        rh = entity.size[1]

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
        distance = sqrt((distx * distx) + (disty * disty))

        if distance <= r:
            return True


    def create_explosive_particles(self):
        number_of_particles = randrange(3, 30, 1)

        for i in range(number_of_particles):
            size = randrange(1, 2, 1)
            pos = self.position

            velocity_x = triangular(-1, 1)
            velocity_y = triangular(-1, 1)

            particle = Particle(self.engine, None, (size, size), len(self.engine.entityMgr.particles), self.engine.gfxMgr.window, pos, (velocity_x, velocity_y), self.color)
            self.engine.entityMgr.particles.append(particle)


    def in_camera(self):
        result = False
        
        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfxMgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfxMgr.scroll[1]:
                result = True

        return result

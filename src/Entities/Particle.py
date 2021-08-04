# IMPORTS #

# Libraries #
from pygame import draw

# Custom Imports #
from .Entity import Entity


class Particle(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, velocity, particle_color):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Particle"

        self.velocity = velocity

        self.position = position
        
        self.color = particle_color
        
        self.time_alive = 0

        self.lifetime_max = self.engine.config.bullet_particle_lifetime


    def draw(self):
        if self.in_camera():
            draw.circle(self.display_surface, self.color, (self.position[0] - self.engine.gfxMgr.scroll[0] + self.size[0] / 2, self.position[1] - self.engine.gfxMgr.scroll[1] + self.size[1] / 2), self.size[0])

    
    def tick(self, dt):
        Entity.tick(self, dt)

        self.time_alive = self.time_alive + self.engine.clock.get_time()
        
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)

        result = self.still_alive()
        
        return result


    def still_alive(self):
        result = False

        if self.time_alive / 1000 < self.lifetime_max:
            result = True
        
        return result

    def in_camera(self):
        result = False

        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfxMgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfxMgr.scroll[1]:
                result = True
        
        return result
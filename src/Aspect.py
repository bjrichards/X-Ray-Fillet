# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame


# Classes
class Aspect():
    def __init__(self, entity):
        self.entity = entity
    

    def shutdown(self):
        pass


    def tick(self, dt):
        pass



class Renderable(Aspect):
    def tick(self, dt):
        pass



class Physics2D(Aspect):
    def tick(self, dt):
        vely = 0
        velx = 0
        if self.entity.engine.config.gravity_on and self.entity.is_grounded == False:
            vely = self.entity.velocity[1] - (self.entity.engine.config.gravity * dt)
            if vely > 1:
                vely = 1
        
        if self.entity.moving_right:
            velx = 0.5
        elif self.entity.moving_left:
            velx = -0.5
        else:
            velx = 0

        self.entity.velocity = (velx, vely)
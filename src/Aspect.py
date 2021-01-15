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
            vely = self.entity.velocity[1] - (self.entity.engine.gravity * dt)
            if vely > 1:
                vely = 1
        
        if self.entity.moving_right:
            velx = self.entity.max_velocity[0]
        elif self.entity.moving_left:
            velx = -self.entity.max_velocity[0]
        else:
            velx = 0

        if self.entity.max_velocity[0] < abs(velx):
            if velx < 0:
                velx = -self.entity.max_velocity[0]
            else:
                velx = self.entity.max_velocity[0]
        
        if self.entity.max_velocity[1] < abs(vely):
            if vely < 0:
                vely = -self.entity.max_velocity[1]
            else:
                vely = self.entity.max_velocity[1]

        self.entity.velocity = (velx, vely)
# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


###########
# Imports #
###########
import pygame


# Classes
class Aspect():
    """ 
    Class used as base Aspect to be inherited from.

    ...

    Attributes
    ----------
    entity : object of Entity Class
        the parent entity this aspect is part of

    Methods
    -------
    tick(dt)
        Update function
    """

    def __init__(self, entity):
        self.entity = entity
    

    def shutdown(self):
        pass


    def tick(self, dt):
        pass


class Physics2D(Aspect):
    """ 
    Class used to calculate 2D physics of parent Entity

    Inherits from Aspect class. To be added to any entity that is
    affected by physics. Calculates and applies the gravity, collision
    detection, and puts the ceiling on velocities. 
    ...

    Attributes
    ----------
    entity : object of Entity Class
        the parent entity this aspect is part of

    Methods
    -------
    tick(dt)
        Update function.

        Calculates new position based on gravity, velocity, and 
        collisions.
        
    """

    def tick(self, dt):
        vely = 0
        velx = 0
        if self.entity.engine.config.gravity_on == True: # and self.entity.is_grounded == False:
            vely = self.entity.velocity[1] - (self.entity.engine.gravity * dt)
        
        
        velx, vely = self.keep_in_parameters(velx, vely)

        posx, posy, velx, vely = self.collisions(velx, vely, dt)

        self.entity.velocity = (velx, vely)
        self.entity.position = (posx, posy)


    def collisions(self, velx, vely, dt):
        collision = False
        check_all = True
        if self.entity.entity_type == "Player":
            check_all = False

        # First check for any horizontal collisions
        next_xpos = self.entity.position[0] + velx * dt
        for platform in self.entity.engine.entityMgr.platforms:
            if not check_all and not platform.in_camera():
                pass
            elif platform.pType != self.entity.block_exlusion: 
                if next_xpos  + self.entity.size[0] > platform.position[0] and next_xpos < platform.position[0] + platform.size[0] and self.entity.position[1] + self.entity.size[1]> platform.position[1] and self.entity.position[1] < platform.position[1] + platform.size[1]:
                    if velx > 0:
                        velx = 0
                        next_xpos = platform.position[0] - self.entity.size[0]
                    elif velx < 0:
                        velx = 0
                        next_xpos = platform.position[0] + platform.size[0]
                    break

        # Now check for any vertical collisions
        next_ypos = self.entity.position[1] + vely * dt
        for platform in self.entity.engine.entityMgr.platforms:
            if not check_all and not platform.in_camera():
                pass
            elif platform.pType != self.entity.block_exlusion: 
                if next_xpos  + self.entity.size[0] > platform.position[0] and next_xpos < platform.position[0] + platform.size[0] and next_ypos + self.entity.size[1] > platform.position[1] and next_ypos < platform.position[1] + platform.size[1]:
                    if vely > 0:
                        vely = 0
                        next_ypos = platform.position[1] - self.entity.size[1]
                        collision = True
                        self.entity.jump = 0
                        jump = 0
                        self.entity.is_grounded = True
                    elif vely < 0:
                        vely = 0
                        next_ypos = platform.position[1] + platform.size[1]
                    
                    break   
        
        if not collision:
            self.entity.is_grounded = False
        
                
        return next_xpos, next_ypos, velx, vely
        

    def keep_in_parameters(self, velx, vely):
        if self.entity.moving_right:
            velx = self.entity.max_velocity[0]
        elif self.entity.moving_left:
            velx = -self.entity.max_velocity[0]
        else:
            velx = 0
        
        if self.entity.max_velocity[1] < abs(vely):
            if vely < 0:
                vely = -self.entity.max_velocity[1]
            else:
                vely = self.entity.max_velocity[1]

        return velx, vely
        
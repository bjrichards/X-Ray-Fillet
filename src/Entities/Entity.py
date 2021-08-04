# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame

# Class
class Entity():
    def __init__(self, engine, image_file_name, size, identity, display):
        self.engine = engine

        self.entity_type = "Entity"
        self.image_file_name = image_file_name

        self.display_surface = display

        self.block_exlusion = None

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

# IMPORTS #

# Libraries #
from pygame import Rect, draw

# Custom Imports #
from .Entity import Entity

class Sprite(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, image_size):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "tile"

        self.source_name = None
        self.source_type = None

        self.image_size = (image_size[0] * self.engine.config.scale, image_size[1] * self.engine.config.scale)
        
        self.color = (255, 255, 255)
        self.position = position
        self.rect = Rect(self.position[0], self.position[1], 64, 64)

        self.image = image_file_name       

        self.selected = False

    def draw(self, dt, is_placed):
        if is_placed:
            if self.in_camera():
                scroll = self.engine.gfx_mgr.scroll
                position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
                self.display_surface.blit(self.image, position)
                # self.display_surface.blit(self.image, self.position)
        else:                
            scroll = [0, 0]
            position = self.position
            self.display_surface.blit(self.image, position)
            if self.selected:
                draw.rect(self.display_surface, self.color, self.rect, 3)

    def is_clicked(self, mouse_position):
        result = False
        if mouse_position[0] > self.position[0] and mouse_position[0] < self.position[0] + 64:
            if mouse_position[1] > self.position[1] and mouse_position[1] < self.position[1] + 64:
                result = True
        
        return result

    def in_camera(self):
        result = False
        
        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfx_mgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfx_mgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfx_mgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfx_mgr.scroll[1]:
                result = True

        return result
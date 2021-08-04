# IMPORTS #

# Libraries #
from pygame import Rect, draw, transform

# Custom Imports #
from .Entity import Entity

class Platform(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, pType):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = (100, 255, 100)
        self.position = position
        self.rect = Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.image = None
        self.pType = pType
        if self.pType != 'I':
            self.image = image_file_name
            self.size = (self.image.get_size()[0] * self.engine.config.scale, self.image.get_size()[1] * self.engine.config.scale)
            self.image = transform.scale(self.image, self.size)

    def draw(self):
        if self.in_camera() and self.pType != 'I':
            scroll = self.engine.gfxMgr.scroll
            position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
            self.display_surface.blit(self.image, position)

            if self.engine.config.bounding_boxes:
                self.rect = Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])
                draw.rect(self.display_surface, self.color, self.rect)
            self.engine.gfxMgr.platforms_rendered += 1


    def in_camera(self):
        result = False
        
        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfxMgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfxMgr.scroll[1]:
                result = True

        return result
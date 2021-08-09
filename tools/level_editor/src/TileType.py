# IMPORTS #

# Libraries #
from pygame import Rect, draw, transform

# Custom Imports #
from .Entity import Entity

class TileType(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, pType):
        Entity.__init__(self, engine, image_file_name, size, identity, display)

        self.color = (100, 255, 100)
        self.position = position
        self.rect = Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.image = None
        self.pType = pType

    def draw(self):
        if self.in_camera():
            scroll = self.engine.gfxMgr.scroll
            position = (self.position[0] - scroll[0], self.position[1] - scroll[1])
            self.display_surface.blit(self.image, position)


    def in_camera(self):
        result = False
        
        if self.position[0] <= self.engine.config.window_size[0] + self.engine.gfxMgr.scroll[0] and self.position[0] + self.size[0] >= self.engine.gfxMgr.scroll[0]:
            if self.position[1] <= self.engine.config.window_size[1] + self.engine.gfxMgr.scroll[1] and self.position[1] + self.size[1] >= self.engine.gfxMgr.scroll[1]:
                result = True

        return result
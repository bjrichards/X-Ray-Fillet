# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
from .sprites import Sprite


# Class
class EntityMgr():
    def __init__(self, engine):
        self.engine = engine

        pass

    
    def initialize(self):        
        self.tile_types = []
        self.sprites = []
        self.layer_0_placed_sprites = []

    def load_map(self):
        pass
    
    def tick(self, dt):
        pass

    def shutdown(self):
        pass
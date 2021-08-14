# Created by Braeden Richards
# Created on August 5th, 2021

# INCLUDES #
from pygame import display, Surface
from pygame import init, quit
from pygame import SRCALPHA


# Class
class GfxMgr():
    def __init__(self, engine):
        self.engine         = engine

        self.window         = None
        self.select_window  = None
        self.screen         = None
        self.screen_size    = None
        
        self.window_pos     = (0,0)
        self.select_pos     = (0,0)
        
    
    def initialize(self, name, size):
        init() # pygame.init()
        display.set_caption(name) # pygame.display
        
        self.screen = display.set_mode(size)
        self.screen_size = self.screen.get_size()

        self.window = Surface((self.screen_size[0] - (self.screen_size[0] / 5), 
                                self.screen_size[1]), SRCALPHA)
        self.window_pos = (self.window_pos[0] + self.screen_size[0] / 5, self.window_pos[1])
        self.select_window = Surface((self.screen_size[0] / 5, self.screen_size[1]), SRCALPHA)

    
    def tick(self, dt):
        self.screen.fill((0,0,0,0))
        self.window.fill((0,0,0))
        self.select_window.fill((150, 150, 150))

        for sprite in self.engine.entity_mgr.sprites:
            sprite.draw(dt)
        
        for sprite in self.engine.entity_mgr.layer_0_placed_sprites:
            sprite.draw(dt)

        self.screen.blit(self.window, self.window_pos)
        self.screen.blit(self.select_window, self.select_pos)

        display.update()

    def shutdown(self):
        quit() # pygame.quit
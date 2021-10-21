# Created by Braeden Richards
# Created on August 5th, 2021

# INCLUDES #
from pygame import display, Surface
from pygame import init, quit
from pygame import SRCALPHA, Color, font


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
        
        self.scroll         = [0,0]

        self.camera_speed   = 0.8
    
    def initialize(self, name, size):
        init() # pygame.init()
        display.set_caption(name) # pygame.display
        
        self.screen = display.set_mode(size)
        self.screen_size = self.screen.get_size()

        self.window = Surface((self.screen_size[0] - (self.screen_size[0] / 5), 
                                self.screen_size[1]), SRCALPHA)
        self.window_pos = (self.window_pos[0] + self.screen_size[0] / 5, self.window_pos[1])
        self.select_window = Surface((self.screen_size[0] / 5, self.screen_size[1]), SRCALPHA)

        self.font = font.SysFont("Arial", 18)

    
    def tick(self, dt):
        if self.engine.app_mgr.moving_right:
            self.scroll[0] += self.camera_speed * dt
        elif self.engine.app_mgr.moving_left:
            self.scroll[0] -= self.camera_speed * dt

        if self.engine.app_mgr.moving_up:
            self.scroll[1] -= self.camera_speed * dt
        elif self.engine.app_mgr.moving_down:
            self.scroll[1] += self.camera_speed * dt

        self.screen.fill((0,0,0,0))
        self.window.fill((0,0,0))
        self.select_window.fill((150, 150, 150))

        for sprite in self.engine.entity_mgr.sprites:
            sprite.draw(dt, False)
        
        for sprite in self.engine.entity_mgr.layer_0_placed_sprites:
            sprite.draw(dt, True)

        for sprite in self.engine.entity_mgr.layer_1_placed_sprites:
            sprite.draw(dt, True)

        self.screen.blit(self.window, self.window_pos)
        self.screen.blit(self.select_window, self.select_pos)

        self.screen.blit(self.update_game_layer(), (900, 0))

        display.update()

    def shutdown(self):
        quit() # pygame.quit


    def update_game_layer(self):
        layer = str(self.engine.app_mgr.selected_layer)
        result = self.font.render("Game Status: " + layer, 1, Color("coral"))
        return result
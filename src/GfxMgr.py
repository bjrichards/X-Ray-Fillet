# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame


# Class
class GfxMgr():
    def __init__(self, engine):
        self.window = None
        self.engine = engine

        self.font = None

        self.window_pos = (0,0)

    
    def initialize(self, name, size):
        pygame.init()
        pygame.display.set_caption(name)
        
        self.screen = pygame.display.set_mode(size)
        self.window = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.uiScreen = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        self.font = pygame.font.SysFont("Arial", 18)


    def tick(self, dt):

        self.screen.fill((0,0,0,0))
        self.window.fill((0,0,0,0))
        self.uiScreen.fill((0,0,0,0))

        self.engine.entityMgr.player.draw()
        
        self.engine.uiMgr.tick(dt)

        for platform in self.engine.entityMgr.platforms:
            platform.draw()

        self.engine.entityMgr.player.draw()
        self.screen.blit(self.window, self.window_pos)
        self.screen.blit(self.uiScreen, (0,0))

        pygame.display.update()

    def shutdown(self):
        pygame.quit()


    def update_fps(self):
        fps = str(int(self.engine.clock.get_fps()))
        result = self.font.render("FPS Count: " + fps, 1, pygame.Color("coral"))
        return result

    def update_is_grounded(self):
        col = str(self.engine.entityMgr.player.is_grounded)
        result = self.font.render("Is Grounded: " + col, 1, pygame.Color("coral"))
        return result

    def update_double_jump(self):
        db = str(self.engine.entityMgr.player.double_jumped)
        result = self.font.render("Double Jumped: " + db, 1, pygame.Color("coral"))
        return result
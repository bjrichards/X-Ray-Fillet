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
        
        self.scroll = [0,0]

        self.scroll_locked = False

        self.platforms_rendered = 0

    
    def initialize(self, name, size):
        pygame.init()
        pygame.display.set_caption(name)
        
        self.screen = pygame.display.set_mode(size)
        self.window = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.uiScreen = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        self.font = pygame.font.SysFont("Arial", 18)


    def tick(self, dt):

        if self.scroll_locked == False:
            self.scroll[0] += ((self.engine.entityMgr.player.position[0] - self.scroll[0]) - self.engine.config.window_size[0] / 2 + self.engine.entityMgr.player.size[0] / 2) / 80    
            # print(abs(self.scroll[0] + self.engine.config.window_size[0]/2 - self.engine.entityMgr.player.position[0]))
            if abs(self.scroll[0] + self.engine.config.window_size[0]/2 - self.engine.entityMgr.player.position[0]) < 40:
                self.scroll_locked = True
        else:
            self.scroll[0] += ((self.engine.entityMgr.player.position[0] - self.scroll[0]) - self.engine.config.window_size[0] / 2 + self.engine.entityMgr.player.size[0] / 2) / 20

        self.screen.fill((0,0,0,0))
        self.window.fill((0,0,0,0))
        self.uiScreen.fill((0,0,0,0))

        self.engine.entityMgr.player.draw()
        
        self.engine.uiMgr.tick(dt)

        self.platforms_rendered = 0
        for platform in self.engine.entityMgr.platforms:
            platform.draw()

        for bullet in self.engine.entityMgr.bullets:
            bullet.draw()

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

    def update_show_jumps(self):
        jumps = str(self.engine.entityMgr.player.jump + 2 % 2)
        result = self.font.render("Jumps Left: " + jumps, 1, pygame.Color("coral"))
        return result


    def update_bullet_count(self):
        bc = str(len(self.engine.entityMgr.bullets))
        result = self.font.render("Bullet Count: " + bc, 1, pygame.Color("coral"))
        return result


    def update_platforms_rendered(self):
        pr = str(self.platforms_rendered)
        result = self.font.render("Platforms Rendered: " + pr, 1, pygame.Color("coral"))
        return result

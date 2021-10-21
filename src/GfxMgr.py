# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
from pygame import Color, display, font, Surface
from pygame import init, quit
from pygame import SRCALPHA


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
        self.enemies_rendered = 0

    
    def initialize(self, name, size):
        init() # pygame.init()
        display.set_caption(name) # pygame.display
        
        self.screen = display.set_mode(size)
        self.window = Surface(self.screen.get_size(), SRCALPHA)
        self.uiScreen = Surface(self.screen.get_size(), SRCALPHA)

        self.font = font.SysFont("Arial", 18)


    def tick(self, dt):
        
        self.screen.fill((0,0,0,0))
        self.window.fill((0,0,0,0))
        self.uiScreen.fill((0,0,0,0))

        if self.engine.gameMgr.game_status == 'ENTRY_ANIMATION' or self.engine.gameMgr.game_status == 'IN_GAME':
            if self.scroll_locked == False:
                self.scroll[0] += ((self.engine.entityMgr.player.position[0] - self.scroll[0]) - self.engine.config.window_size[0] / 2 + self.engine.entityMgr.player.size[0] / 2) / 100    
                self.scroll[1] += ((self.engine.entityMgr.player.position[1] - self.scroll[1]) - self.engine.config.window_size[1] / 2 + self.engine.entityMgr.player.size[1] / 2) / 100    
                if abs(self.scroll[0] + self.engine.config.window_size[0]/2 - self.engine.entityMgr.player.position[0]) < 40:
                    self.scroll_locked = True
                    self.engine.gameMgr.game_status = 'IN_GAME'
            else:
                self.scroll[0] += ((self.engine.entityMgr.player.position[0] - self.scroll[0]) - self.engine.config.window_size[0] / 2 + self.engine.entityMgr.player.size[0] / 2) / 20
                self.scroll[1] += ((self.engine.entityMgr.player.position[1] - self.scroll[1]) - self.engine.config.window_size[1] / 2 + self.engine.entityMgr.player.size[1] / 2) / 20
                


            self.platforms_rendered = 0
            for platform in self.engine.entityMgr.platforms_layer_0:
                platform.draw()
            for platform in self.engine.entityMgr.platforms_layer_1:
                platform.draw()

            self.enemies_rendered = 0
            for enemy in self.engine.entityMgr.enemies:
                enemy.draw()

            for bullet in self.engine.entityMgr.bullets:
                bullet.draw()

            for particle in self.engine.entityMgr.particles:
                particle.draw()

            self.engine.entityMgr.player.draw(dt)

        self.engine.uiMgr.tick(dt)

        self.screen.blit(self.window, self.window_pos)
        self.screen.blit(self.uiScreen, (0,0))

        display.update()

    def shutdown(self):
        quit() # pygame.quit


    def update_fps(self):
        fps = str(int(self.engine.clock.get_fps()))
        result = self.font.render("FPS Count: " + fps, 1, Color("coral"))
        return result

    def update_is_grounded(self):
        col = str(self.engine.entityMgr.player.is_grounded)
        result = self.font.render("Is Grounded: " + col, 1, Color("coral"))
        return result

    def update_show_jumps(self):
        jumps = str(2 - self.engine.entityMgr.player.jump)
        result = self.font.render("Jumps Left: " + jumps, 1, Color("coral"))
        return result


    def update_bullet_count(self):
        bc = str(len(self.engine.entityMgr.bullets))
        result = self.font.render("Bullet Count: " + bc, 1, Color("coral"))
        return result


    def update_platforms_rendered(self):
        pr = str(self.platforms_rendered)
        result = self.font.render("Platforms Rendered: " + pr, 1, Color("coral"))
        return result


    def update_enemy_count(self):
        pr = str(len(self.engine.entityMgr.enemies))
        result = self.font.render("Enemy Count: " + pr, 1, Color("coral"))
        return result


    def update_enemy_rendered_count(self):
        pr = str(self.enemies_rendered)
        result = self.font.render("Enemies Rendered: " + pr, 1, Color("coral"))
        return result

    def update_player_lives_left(self):
        pr = str(self.engine.gameMgr.player_lives)
        result = self.font.render("Player Lives: " + pr, 1, Color("coral"))
        return result

    def update_game_status(self):
        pr = str(self.engine.gameMgr.game_status)
        result = self.font.render("Game Status: " + pr, 1, Color("coral"))
        return result

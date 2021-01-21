# Created by Braeden Richards
# Created on January 7th, 2021
# Desc:


# Includes
import pygame
from .Button import Button


# Class
class UiMgr():
    def __init__(self, engine):
        self.engine = engine

        self.in_game = None
        self.show_fps = None
        self.show_grounded = None
        self.show_jumps_left = None
        self.show_game_status = None
        self.show_bullet_count = None
        self.show_total_enemy_count = None
        self.show_platforms_rendered = None
        self.show_total_enemy_rendered = None
       
        self.main_menu_buttons = None
        
    
    def initialize(self):
        self.in_game = False
        self.show_fps = self.engine.config.show_fps
        self.show_grounded = self.engine.config.show_is_grounded
        self.show_jumps_left = self.engine.config.show_jumps_left
        self.show_game_status = self.engine.config.show_game_status
        self.show_bullet_count = self.engine.config.show_bullet_count
        self.show_total_enemy_count = self.engine.config.show_total_enemy_count
        self.show_platforms_rendered = self.engine.config.show_platforms_rendered
        self.show_total_enemy_rendered = self.engine.config.show_total_enemy_rendered

        self.main_menu_buttons = []

        start_game_button = Button('START', self.engine.config.start_game_button_0, 
                                ((self.engine.config.window_size[0] / 2) - 75, 
                                    (self.engine.config.window_size[1] / 2) - 32), 
                                self.engine.gfxMgr.window, 
                                (150, 75))
        self.main_menu_buttons.append(start_game_button)


    def tick(self, dt):
        if self.engine.gameMgr.game_status == 'IN_GAME' or self.engine.gameMgr.game_status == 'ENTRY_ANIMATION':
            if self.show_fps:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_fps(), (10, 0))
            if self.show_grounded:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_is_grounded(), (300, 0))
            if self.show_jumps_left:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_show_jumps(), (600, 0))
            if self.show_bullet_count:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_bullet_count(), (900, 0))
            if self.show_platforms_rendered:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_platforms_rendered(), (10, 50))
            if self.show_total_enemy_count:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_enemy_count(), (300, 50))
            if self.show_total_enemy_rendered:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_enemy_rendered_count(), (600, 50))
            if self.show_game_status:
                self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_game_status(), (900, 50))
            
            self.engine.gfxMgr.uiScreen.blit(self.engine.gfxMgr.update_player_lives_left(), (10, 100))

        elif self.engine.gameMgr.game_status == 'MENU':
            transparent_background = pygame.Surface((self.engine.config.window_size[0], self.engine.config.window_size[1]))
            transparent_background = transparent_background.convert_alpha()
            transparent_background.fill((0, 0, 0, 60))
            self.engine.gfxMgr.uiScreen.blit(transparent_background, (0, 0))

            for button in self.main_menu_buttons:
                button.draw()

    def shutdown(self):
        pass
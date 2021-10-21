# Created by Braeden Richards
# Created on August 5th, 2021

# INCLUDES #
from pygame import event, mouse
from pygame import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_0, K_1, MOUSEBUTTONDOWN
from pygame.constants import K_d, K_a, K_w, K_s


# Class
class InputMgr():
    def __init__(self, engine):
        self.engine = engine

    def initialize(self):
        pass

    def tick(self, dt):
        for single_event in event.get():
            if single_event.type == QUIT:
                self.engine.keep_running = False
            
            # Key downs
            elif single_event.type == KEYDOWN:
                # Escape Key (exit game)
                if single_event.key == K_ESCAPE:
                    self.engine.keep_running = False

                # Changing selected layer
                elif single_event.key == K_0:
                    self.engine.app_mgr.selected_layer = 0
                elif single_event.key == K_1:
                    self.engine.app_mgr.selected_layer = 1
                
                # Movement of camera
                elif single_event.key == K_d:
                    self.engine.app_mgr.moving_right = True
                elif single_event.key == K_a:
                    self.engine.app_mgr.moving_left = True
                elif single_event.key == K_w:
                    self.engine.app_mgr.moving_up = True
                elif single_event.key == K_s:
                    self.engine.app_mgr.moving_down = True

            # Key Ups
            elif single_event.type == KEYUP:
                if single_event.key == K_d:
                    self.engine.app_mgr.moving_right = False
                elif single_event.key == K_a:
                    self.engine.app_mgr.moving_left = False
                elif single_event.key == K_w:
                    self.engine.app_mgr.moving_up = False
                elif single_event.key == K_s:
                    self.engine.app_mgr.moving_down = False

            # Mouse downs
            elif single_event.type == MOUSEBUTTONDOWN:
                if self.engine.app_mgr.app_status == 'MAIN':
                    if single_event.button == 1:
                        # print(self.engine.gfx_mgr.select_window.get_size())
                        if mouse.get_pos()[0] < self.engine.gfx_mgr.select_window.get_size()[0]:
                            for sprite in self.engine.entity_mgr.sprites:
                                if sprite.is_clicked(mouse.get_pos()):
                                    if self.engine.app_mgr.selected_sprite != None:
                                        self.engine.app_mgr.selected_sprite.selected = False
                                    sprite.selected = True
                                    self.engine.app_mgr.selected_sprite = sprite
                                    break
                        else:
                            self.engine.app_mgr.place_block(mouse.get_pos())
                    elif single_event.button == 3:
                        if mouse.get_pos()[0] < self.engine.gfx_mgr.select_window.get_size()[0]:
                            if self.engine.app_mgr.selected_sprite != None:
                                self.engine.app_mgr.selected_sprite.selected = False
                                self.engine.app_mgr.selected_sprite = None
                        else:
                            self.engine.app_mgr.remove_block(mouse.get_pos())


    def shutdown(self):
        pass
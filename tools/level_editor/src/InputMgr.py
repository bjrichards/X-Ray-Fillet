# Created by Braeden Richards
# Created on August 5th, 2021

# INCLUDES #
from pygame import event, mouse
from pygame import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN


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
            elif single_event.type == KEYDOWN:
                # Escape Key (exit game)
                if single_event.key == K_ESCAPE:
                    self.engine.keep_running = False
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
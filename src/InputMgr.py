# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
from pygame import event,  mouse
from pygame import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_SPACE, MOUSEBUTTONDOWN
from pygame import K_a, K_d, K_s, K_w


# Class
class InputMgr():
    def __init__(self, engine):
        self.engine = engine

    
    def initialize(self):
        pass


    def tick(self):
        for single_event in event.get():
            # Window is 'X'ed out
            if single_event.type == QUIT:
                self.engine.keepRunning = False

            elif single_event.type == KEYDOWN:
                # Escape Key (exit game)
                if single_event.key == K_ESCAPE:
                        self.engine.keepRunning = False
                if self.engine.gameMgr.game_status == 'IN_GAME':
                    if single_event.key == K_SPACE or single_event.key == K_w:
                        self.engine.entityMgr.player.jump_()
                    
                    elif single_event.key == K_a:
                        self.engine.entityMgr.player.moving_left = True
                    elif single_event.key == K_d:
                        self.engine.entityMgr.player.moving_right = True
                    elif single_event.key == K_s:
                        self.engine.entityMgr.player.down_button = True

            elif single_event.type == KEYUP:
                if self.engine.gameMgr.game_status == 'IN_GAME':
                    if single_event.key == K_a:
                        self.engine.entityMgr.player.moving_left = False
                    elif single_event.key == K_d:
                        self.engine.entityMgr.player.moving_right = False
                    elif single_event.key == K_s:
                        self.engine.entityMgr.player.down_button = False

            elif single_event.type == MOUSEBUTTONDOWN:
                if self.engine.gameMgr.game_status == 'IN_GAME':
                    if single_event.button == 1:
                        self.engine.entityMgr.player.fire(mouse.get_pos())
                elif self.engine.gameMgr.game_status == 'MENU':
                    if single_event.button == 1:
                        for button in self.engine.uiMgr.main_menu_buttons:
                            if button.is_clicked(mouse.get_pos()):
                                if button.button_id == 'START':
                                    self.engine.gameMgr.game_status = 'START'
                                    break

    def shutdown(self):
        pass
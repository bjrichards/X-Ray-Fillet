# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame


# Class
class InputMgr():
    def __init__(self, engine):
        self.engine = engine

        pass

    
    def initialize(self):
        pass


    def tick(self):
        for event in pygame.event.get():
            # Window is 'X'ed out
            if event.type == pygame.QUIT:
                self.engine.keepRunning = False

            elif event.type == pygame.KEYDOWN:
                # Escape Key (exit game)
                if event.key == pygame.K_ESCAPE:
                    self.engine.keepRunning = False

                elif event.key == pygame.K_SPACE:
                    self.engine.entityMgr.player.jump_()

                elif event.key == pygame.K_a:
                    self.engine.entityMgr.player.moving_left = True
                elif event.key == pygame.K_d:
                    self.engine.entityMgr.player.moving_left = False
                    self.engine.entityMgr.player.moving_right = True
                elif event.key == pygame.K_s:
                    self.engine.entityMgr.player.down_button = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.engine.entityMgr.player.moving_left = False
                elif event.key == pygame.K_d:
                    self.engine.entityMgr.player.moving_right = False
                elif event.key == pygame.K_s:
                    self.engine.entityMgr.player.down_button = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.engine.entityMgr.player.fire(pygame.mouse.get_pos())

    def shutdown(self):
        pass
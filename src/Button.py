# Created by Braeden Richards
# Created on January 7th, 2021
# Desc:


# Includes
import pygame


# Class
class Button():
    def __init__(self, button_id, image_file_name, position, surface, size):
        self.button_id = button_id
        self.size = size
        self.surface = surface
        self.position = position

        self.image = pygame.image.load(image_file_name).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, self.size)

        self.image_rect = self.image.get_rect()
    

    def draw(self):
        self.surface.blit(self.image, self.position)


    def is_clicked(self, mouse_position):
        result = False

        if mouse_position[0] > self.position[0] and mouse_position[0] < self.position[0] + self.size[0]:
            if mouse_position[1] > self.position[1] and mouse_position[1] < self.position[1] + self.size[1]:
                result = True

        return result
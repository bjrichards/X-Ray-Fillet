# Created by Braeden Richards
# Created on January 7th, 2021
# Desc: Button class used for creating, drawing, and checking for a click
#       on the button

############
# Includes #
############
import pygame   # For image loading, blitting


# Class
class Button():
    """ 
    Class containing the needed functions for creation and use of buttons

    ...

    Attributes
    ----------
    button_id: int
        integer representing a unique id for the button
    position: tuple (int, int)
        two integers representing the x, y position of the button in a
        2 dimensional world
    size: tuple (int, int)
        two integers representing the horizontal, vertical sizes of the
        button

    Methods
    -------
    draw()
        Function to blit button on screen

    is_clicked(mouse_position):
        Checks whether the button was clicked

        Uses the mouse position to check if the mouse is within the
        bounds of the button  
        
        Returns
        -------
            bool
                true if mouse position is within the bounds fo the 
                button
    """
    def __init__(self, button_id, image_file_name, position, surface, size):
        """
        Parameters
        ----------
        button_id: int
            integer representing a unique id for the button
        image_file_name: str
            the name and path of the file containing the sprite image
        position: tuple (int, int)
            two integers representing the x, y position of the button in a
            2 dimensional world
        surface: pygame.surface
            surface the button will be drawn/blitted onto
        size: tuple (int, int)
            two integers representing the horizontal, vertical sizes of the
            button
        """

        self.button_id = button_id
        self.size = size
        self.surface = surface
        self.position = position

        self.image = pygame.image.load(image_file_name).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, self.size)

        self.image_rect = self.image.get_rect()
    

    def draw(self):
        """Draws self onto self.surface
        """

        self.surface.blit(self.image, self.position)


    def is_clicked(self, mouse_position):
        """
        Parameters
        ----------
        mouse_position: tuple (int, int)
            x, y position of the mouse when the mouse button was clicked

        Returns
        -------
            bool
                true if mouse position is within the bounds fo the 
                button
        """

        result = False

        if mouse_position[0] > self.position[0] and mouse_position[0] < self.position[0] + self.size[0]:
            if mouse_position[1] > self.position[1] and mouse_position[1] < self.position[1] + self.size[1]:
                result = True

        return result
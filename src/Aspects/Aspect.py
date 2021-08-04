# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


###########
# Imports #
###########

# Classes
class Aspect():
    """ 
    Class used as base Aspect to be inherited from.

    ...

    Attributes
    ----------
    entity : object of Entity Class
        the parent entity this aspect is part of

    Methods
    -------
    tick(dt)
        Update function
    """

    def __init__(self, entity):
        self.entity = entity
    

    def shutdown(self):
        pass


    def tick(self, dt):
        pass
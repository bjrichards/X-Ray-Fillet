import pygame

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to laod spritesheet image: {filename}")
            raise SystemExit(e)
    
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height], pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), (x, y, width, height))
        return image.convert()
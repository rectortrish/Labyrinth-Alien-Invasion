# alien class

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    #A class to represent a single alien in the fleet

    def __init__ (self, ai_game):
        #initialize the alien and set its starting position

        super().__init__()
        self.screen = ai_game.screen

        #load the alien image and set its rect

        self.image = pygame.image.load("Images/alien.bmp")
        self.rect = self.image.get_rect()

        #start each new alien at the top left of the screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        

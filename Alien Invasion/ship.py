# Creating the Ship Class

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #A class to manage the ship

    def __init__ (self, ai_game):
        super().__init__()
        
        #Initialize the ship and set its starting position
        self.screen = ai_game.screen
        
        self.settings = ai_game.settings
        
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and gets its rect
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


        self.x = float(self.rect.x)

        #Movement Flag

        self.moving_right = False      
        self.moving_left = False



    def update(self):
        #update the ship's position based on the movement flag

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float (self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

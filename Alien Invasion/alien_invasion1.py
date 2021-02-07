# Creating the Pygame Window and Responding to User Input

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Overall class to manage game assest and behavior'''

    def __init__(self):
        #Initialize the game and create the games resources

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption ("Alien Invasion")
        self.ship = Ship(self)

    def run_game (self):
        #Start the main loop of the game.
        
        while True:
            
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

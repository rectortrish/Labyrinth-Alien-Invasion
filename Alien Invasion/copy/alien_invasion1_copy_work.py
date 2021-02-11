# Creating the Pygame Window and Responding to User Input

#github comment

import sys
import pygame
from settings_copy_work import Settings
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
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self): #helper method to run_game
            
            #respond to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    
                

    def _update_screen(self): #helper method to run_game
        
        #Update images on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

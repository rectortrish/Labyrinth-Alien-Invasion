# Creating the Pygame Window and Responding to User Input

#github comment

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    '''Overall class to manage game assest and behavior'''

    def __init__(self):
        #Initialize the game and create the games resources

        pygame.init()
        self.settings = Settings()

        #Running the game in full screen mode

        '''self.screen = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height'''      
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption ("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        
    def run_game (self):
        #Start the main loop of the game.
        
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self): #helper method to run_game
            
            #respond to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    def _check_keydown_events(self, event):
                    
                   
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events (self, event):

                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add (new_bullet)
                    
                

    def _update_screen(self): #helper method to run_game
        
        #Update images on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

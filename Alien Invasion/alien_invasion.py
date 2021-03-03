# Creating the Pygame Window and Responding to User Input

#github comment

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        
    def run_game (self):
        #Start the main loop of the game.
        
        while True:
            self._check_events()
            self.ship.update()        
            self._update_screen()
            self._update_aliens()
            self._update_bullets()


    def _update_aliens (self):
        #update the positions of all the aliens in the fleet.
        self._check_fleet_edges()
        self.aliens.update()
            
            

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


    def _create_fleet(self):
        #Create the fleet of aliens

        #make an alien

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        
        #self.aliens.add(alien)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)

        number_rows = available_space_y // (2 * alien_height)

        for row_number in range (number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        #Respond appropriately if any aliens reached an edge

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction (self):
        #Drop the entire fleet and change direction

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
  
    def _create_alien(self, alien_number, row_number):
        
        #Create and alien and place it in its row
    
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

        

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add (new_bullet)
            

    def _update_bullets(self):
        #Update the position of bullets and get rid of old bullets
        
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
   

    def _update_screen(self): #helper method to run_game
        
        #Update images on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
                
            self.aliens.draw (self.screen)
            
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

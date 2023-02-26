# Alien Invasion

# importing the packages needed
import sys
import pygame

# import the settings
from settings import Settings

# import ship
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """manage game assets and behavior"""

    def __init__(self):
        """Initializing the screen/form"""
        pygame.init()

        # creating instance for the class Settings
        self.settings = Settings()

        # Full screen for the game
        # get the size of the screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height=self.screen.get_rect().height
        self.settings.screen_width=self.screen.get_rect().width

        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

        # creating instance for for class Ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Loop for the game"""
        while True:
            self._checks_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # we need to delete the bullets so it will not consume ram
            # length of the bullets in copy() method
            # if the bullets is outside the rect, it will delete that bullet
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

    def _checks_events(self):
        """Respond to kepresses adn mouse events"""
        # monitor in the player wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # checks for keypress
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
               

    def _check_keydown_events(self, event):
        """ Respond to keypress """
        if event.key ==  pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the shipt to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _check_keyup_events(self, event):
        """ Respond to key release """
        if event.key ==  pygame.K_RIGHT:
            # if the user release his finger from the key
            # stop moving left
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # if the user release his finger from the key
            # stop moving left
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images, flip to the new screen"""
        # bgcolor
        self.screen.fill(self.settings.bg_color)

        # position for the ship
        self.ship.blitme()

        # draw the group bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # screen
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
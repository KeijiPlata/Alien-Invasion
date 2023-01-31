# Alien Invasion

# importing the packages needed
import sys
import pygame

# import the settings
from settings import Settings

# import ship
from ship import Ship

class AlienInvasion:
    """manage game assets and behavior"""

    def __init__(self):
        """Initializing the screen/form"""
        pygame.init()

        # creating instance for the class Settings
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

        # creating instance for for class Ship
        self.ship = Ship(self)

    def run_game(self):
        """Loop for the game"""
        while True:
            self._checks_events()
            self.ship.update()
            self._update_screen()

    def _checks_events(self):
        """Respond to kepresses adn mouse events"""
        # monitor in the player wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # checks for keypress
            elif event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key ==  pygame.K_RIGHT:
                    # if the user release his finger from the key
                    # stop moving
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images, flip to the new screen"""
        # bgcolor
        self.screen.fill(self.settings.bg_color)

        # position for the ship
        self.ship.blitme()
            
        # screen
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
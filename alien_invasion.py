# Alien Invasion
import sys
import pygame

# import the settings
from settings import Settings

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

    def run_game(self):
        """Loop for the game"""
        while True:
            # monitor in the player wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            # screen
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
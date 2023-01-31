"""Creating the player ship"""

# import the package needed
import pygame

class Ship:
    """A class to manage ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # position of the ship
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False

    def update(self):
        """Update the ships position based ont the movement_right attribute"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
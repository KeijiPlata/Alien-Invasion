"""Creating the player ship"""

# import the package needed
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # position of the ship
        self.rect.midbottom = self.screen_rect.midbottom

        # convert x to accept float values
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based ont the movement_right attribute"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object
        self.rect.x = self.x 

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
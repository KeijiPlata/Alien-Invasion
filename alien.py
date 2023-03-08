# import packages needed
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image just like loading the ship
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien exact horizontal location
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        # the movement speed is multiplied by fleet direction
        # if the fleet direction is equal to positive 1, it will move to the 
        # right, and vice versa
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()

        # checks if the alien is in the edge of the screen(left and right)
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        

        

        

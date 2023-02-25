# import the packages needed
import pygame
from pygame.sprite import Sprite

# inherits from sprite
# sprites is used to group related elements in game and act as group
class Bullet(Sprite):
    """ Ship bullets """

    def __init__(self, ai_game):
        """ Create a bullet at the ship current location """
        super().__init__() # inherits from the class Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # initialize the bullet at bullet rect at (0, 0) and then set correct
        # and updated position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        
        # match the attribute of the ship so that it imerge on the top of ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """ Move the bullet up the screen """
        # update the position of the bullet
        # this get the speed of the bullet and subtract it from self.y
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y
        

    def draw_bullet(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
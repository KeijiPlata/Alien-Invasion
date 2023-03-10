"""Settings for  alien_invasion"""

class Settings:
    """Store all the settings of the game"""
    
    def __init__(self):

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
         # ship settings
        self.ship_speed = 1.5

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # direction 1 represents right, -1 represents left
        self.fleet_direction = 1


        
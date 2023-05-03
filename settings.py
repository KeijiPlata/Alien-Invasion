"""Settings for  alien_invasion"""

class Settings:
    """Store all the settings of the game"""
    
    def __init__(self):

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
         # ship settings
        self.ship_speed = 1.5

        # ship life
        self.ship_limit = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # direction 1 represents right, -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 left
        self.fleet_direction = 1

    def increase_speed (self):
        """Increase the speed of the game"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale



        


        
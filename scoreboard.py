import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """report scoring information"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        """Initialize score attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prep image
        self.prep_image()

    def prep_image(self):
        """Prepare images required in alien invasion"""
        # prepare the ship 
        self.prep_ships()

        # prepare the score image
        self.prep_score()

        # prepare the highscore
        self.prep_high_score()

        # prepare the level
        self.prep_level()


    def prep_ships(self):
        """show how many lives you have left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """turn level into rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # position the level below the highscore
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """ turn the highcore into a rendererd image """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_score(self):
        """prepare the score image"""
        # when you pass negative number to second argument to the round function, 
        # it will round the value to the nearest 10, 100, 1000 and so on 
        rounded_score = round(self.stats.score, -1)

        # it is a way of formatting to insert commas into numbers when converting
        # numerical value to a string
        score_str = "{:,}".format(rounded_score)

        
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """display the score and level"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """check if the high score is updated"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
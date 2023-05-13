import pygame.font

class Scoreboard:
    """report scoring information"""

    def __init__(self, ai_game):
        """Initialize score attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the score image
        self.prep_score()
        self.prep_high_score()

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
        """display the score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """check if the high score is updated"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
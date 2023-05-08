class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start the game in inactive state
        self.game_active = False

    def reset_stats(self):
        """reset the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        
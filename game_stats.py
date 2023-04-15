class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """reset the game"""
        self.ship_left = self.settings.ship_limit
        
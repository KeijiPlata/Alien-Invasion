from game_stats import GameStats

class ReadWriteHs:
    """ read or write highscore """
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self._highscore_file = 'highscore.txt'
        self.read_highscore()

    def write_highscore(self):
        """ write highscore to text file """
        with open(self._highscore_file, "w") as file_object:
            file_object.write(str(self.stats.high_score))

    def read_highscore(self):
        """ read highscore from text file """
        with open(self._highscore_file, "r") as file_object:
            self.stats.high_score = int(file_object.read())


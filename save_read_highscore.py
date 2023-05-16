class ReadWriteHs:
    """ read or write highscore """
    def __init__(self):
        self._highscore_file = 'highscore.txt'

    def write_highscore(self):
        """ write highscore to text file """
        with open(self._highscore_file, "w") as file_object:
            file_object.write(str(self._highscore))


__author__ = 'COX1KB'


class chromosome:
    def __init__(self):
        self.number = -1

    def lookupChromosome(self, number, URL):
        if self.number == number:
            return 0
        else:
            self.number = number
            return 100          #downloading data over the internet takes a long time!

    def getSnp(self, position):
        return (1, 'X')     #here, we are *simulating* getting this data out of a data structure.  Use your imagination!

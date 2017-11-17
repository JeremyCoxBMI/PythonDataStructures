__author__ = 'COX1KB'


class chromosome:
    def __init__(self):
        self.number = -1

    def lookupChromosome(self, number, URL):
        #current chromosome is the one you want
        if self.number == number:
            return 0
        #use internet to get a chromosome not in memory
        else:
            self.number = number
            return 100          #downloading data over the internet takes a long time!

    def getSnp(self, position):
        return (1, 'X')     #here, we are *simulating* getting this data out of a data structure.  Use your imagination!

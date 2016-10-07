__author__ = 'COX1KB'

import timeit
import random

#give a random number from 1 to size
def rando(size):
    return random.randint(1,size)


class mytimer:
    """Allows timing code in milliseconds"""
    def __init__(self):
        self.start()

    def __str___(self):
        now = timeit.default_timer()
        return str((now - self.Tstart)*1000)+"ms"

    def __repr___(self):
        now = timeit.default_timer()
        return str((now - self.Tstart)*1000)+"ms"

    def stop(self):
        self.Tstop = timeit.default_timer()

    def start(self):
        self.Tstart = timeit.default_timer()
        self.Tstop = -1

    def elapsed(self):
        if (self.Tstop == -1):
            now = timeit.default_timer()
            return str((now - self.Tstart) * 1000)+"ms"
        else:
            return str((self.Tstop - self.Tstart) * 1000)+"ms"

    def elapsedMilliSeconds(self):
        if (self.Tstop == -1):
            now = timeit.default_timer()
            return (now - self.Tstart) * 1000
        else:
            return str(self.Tstop - self.Tstart) * 1000
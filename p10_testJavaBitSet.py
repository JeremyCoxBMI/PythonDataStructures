from importlib import import_module

__author__ = 'COX1KB'


# When writing my software, I decided to reverse the order of the bits I was storing
# This change was made so that the bitset representing DNA sorted lexographically
# When reading data in, I was now writing data from top of array to bottom
# Look at how the write operation time is not constant (i.e. not O(1))

# What will happen when I run a program and the complexity is not what I thought?
# What is the underlying difference and why did the authors make this choice?
# Why didn't they warn us about it?
# What will happen when I increase from 62 to 250 million bits?



import time

import mytimer as mt



class JavaBitSet:
    def __init__(self):
        self.bits = []

    def append(self,value):
        self.bits.append(value)

    def write(self,index,value):
        if index >= len(self.bits):
            blanks = index - len(self.bits) - 1
            for k in range(0, blanks):
                self.bits.append(0)
            self.bits.append(value)
        else:
            self.bits[index] = value
            self.compressData(index)

    def compressData(self,index):
        #this simulates the time to compress data
        time.sleep(index/10000.0)

    def get(self, index):
        return self.bits[index]


def copyVersionOne(sourceBitSet):
    targetBitSet = JavaBitSet()
    for k in range(0,62):   #0 to 61
        targetBitSet.write(k,sourceBitSet.get(k))
    return targetBitSet


def copyVersionTwo(sourceBitSet):
    targetBitSet = JavaBitSet()
    myrange = range(0,62)
    myrange.reverse()
    for k in myrange:  #0 to 61 in reverse
        targetBitSet.write(k,sourceBitSet.get(k))
    return targetBitSet



#main program
if __name__ == "__main__":

    bitset = JavaBitSet()

    for x in range(0,62):
        bitset.append(mt.rando(2)-1)

    timer = mt.mytimer()

    timer.start()
    copy1 = copyVersionOne(bitset)
    print "CopyVersionOne took "+timer.elapsed()

    timer.start()
    copy2 = copyVersionTwo(bitset)
    print "CopyVersionTwo took "+timer.elapsed()


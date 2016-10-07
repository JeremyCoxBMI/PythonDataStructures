__author__ = 'COX1KB'

#  Theory question: What is worst case scenario for any sort to maximize the work done?
#       Realization: In practice, worst case doesn't exist.
#
# HeapSort is an IN PLACE sort, which means you don't need to ever make a copy
# HeapSort has O(n log n) time
# HeapSort however is not used.
# QuickSort is used all the time, which has
#   Average Case O(n log n)
#   Worst Case O(n^2)
#   Best Case O(n log n)
# Because quick sort is faster.
#
#   BUT WHY?  We always use O(n) to count the "key operation", which is in this case swaps.
#       Swaps are much slower on medium and large data.  Why?  Talk about a clerk and # files on desk.
#   BUT truthfully, it is more complicated than that.  You have to do other operations as well.
#       AND on different computers or programming languages, the same operation may take longer or shorter time
#
# The lesson here is very simple:
# Theory can guide you, but at the end of the day, test and use what is fastest.
#
# Why is quicksort faster?
# Because you can do compare operation much faster than a swap
# Which one would be fastest if the operations were the same time?
# Which one would be fastest if the compare was very slow?


import math

class bubble:
    def __init__(self):
        self.data = []
        self.swaps = 0
        self.compares = 0

    def append(self,value):
        self.data.append(value)

    def getSwaps(self):
        return self.swaps

    def size(self):
        return len(self.data)

    def bubbleSort(self):
        for j in range(0,self.size()-1):
            for k in range(j+1,self.size()):
                self.compares += 1
                if self.data[j] > self.data[k]:
                    self.swap(j, k)

    def swap(self,indexA,indexB):
        self.swaps += 1
        temp = self.data[indexA]
        self.data[indexA] = self.data[indexB]
        self.data[indexB] = temp



class heap:
    def __init__(self):
        self.data = []
        self.swaps = 0
        self.compares = 0

    def append(self,value):
        self.data.append(value)

    def size(self):
        return len(self.data)

    def getSwaps(self):
        return self.swaps

    def heapsort(self):
        self.heapify()
        self.heapToSortedArray()
        self.data.reverse()

    def heapify(self):
        start = self.size() - 1
        end = start
        while start >= 0:
            self.siftDown(start, end)
            start -= 1

    def heapToSortedArray(self):
        currIdx = self.size() - 1

        # here, we are converting the heap starting to an array, working our way from the back
        # currIdx is the index of the position being converted
        while currIdx > 0:
            self.swap(0, currIdx)   #put greatest element at position currIdx
            currIdx -= 1
            self.siftDown(0, currIdx)

    def siftDown(self, start, end):
        root = start
        child = self.leftChild(root)
        while (child <= end):
            swap = root

            if self.data[swap] > self.data[child]:
                swap = child

            rchild = self.rightChild(root)

            if rchild <= end and self.data[swap] > self.data[rchild]:
                swap = rchild

            self.compares += 2

            if (swap != root):
                self.swap(swap,root)
                root = swap
            else:
                break
            child = self.leftChild(root)

    def leftChild(self, index):
        return 2*index+1

    def rightChild(self,index):
        return 2*index+2

    def swap(self,indexA,indexB):
        self.swaps += 1
        temp = self.data[indexA]
        self.data[indexA] = self.data[indexB]
        self.data[indexB] = temp


class quick:
    def __init__(self):
        self.data = []
        self.swaps = 0
        self.compares = 0

    def append(self,value):
        self.data.append(value)

    def size(self):
        return len(self.data)

    def getSwaps(self):
        return self.swaps

    def quickSortHoare(self):
        self.quickSort(0, self.size()-1)

    def quickSort(self,lo,hi):
        if lo < hi:    #this steps for stopping recursion
            p = self.partitionHoare(lo, hi)
            self.quickSort(lo,p)
            self.quickSort(p+1,hi)

    def partitionHoare(self,lo,hi):
        pivot = self.data[lo]
        while(True):
            i = lo
            j = hi
            while(self.data[i] < pivot):
                i += 1
                self.compares += 1
            while(self.data[j] > pivot):
                j -= 1
                self.compares += 1
                self.compares += 2
            if i >= j:
                return j
            self.swap(i,j)

    def pivot(self,lo,hi):
        return lo

    def swap(self,indexA,indexB):
        self.swaps += 1
        temp = self.data[indexA]
        self.data[indexA] = self.data[indexB]
        self.data[indexB] = temp





import mytimer as mt

if __name__ == "__main__":
    bubz = bubble()
    heapy = heap()
    hare = quick()

    numElements = 40
    for x in range(0,numElements):
        y = mt.rando(1000000)
        bubz.append(y)
        heapy.append(y)
        hare.append(y)

    timer = mt.mytimer()
    timer.start()
    bubz.bubbleSort()
    print "BubbleSort took "+timer.elapsed()
    timer.start()
    heapy.heapsort()
    print "HeapSort took   "+timer.elapsed()
    z1 = timer.elapsedMilliSeconds()
    timer.start()
    hare.quickSortHoare()
    print "QuickSort took  "+timer.elapsed()
    z2 = timer.elapsedMilliSeconds()
    print

    print "All three sorted (showing first 20 only)"
    print "%8s" % "bubble","\t","%8s" % "heap","\t","%8s" % "quick"
    for x in range(0,20):
        print "%8d" % bubz.data[x],"\t","%8d" % heapy.data[x],"\t","%8d" % hare.data[x]

    print
    print "n^2 ",numElements**2,"\t\tn log n ",numElements*math.log(numElements, 2)
    print
    print "bubblesort swaps ",bubz.getSwaps()
    print "heapsort swaps   ",heapy.getSwaps()
    print "quicksort swaps  ",hare.getSwaps()
    print
    print "bubblesort compares ",bubz.compares
    print "heapsort compares   ",heapy.compares
    print "quicksort compares  ",hare.compares

    x1 = heapy.getSwaps()
    y1 = heapy.compares
    z1 *= 1000

    x2 = hare.getSwaps()
    y2 = hare.compares
    z2 *= 1000

    m3 = -1.0 * x1 / x2     #NOTE here the goofy way we force integers to floats
                            #This requires foreknowledge that they are in fact integers, because python is weakly typed
    x3 = x2 * m3
    y3 = y2 * m3
    z3 = z2 * m3

    m4 = -1.0 * y1 / y2
    x4 = x2 * m4
    y4 = y2 * m4
    z4 = z2 * m4

    print
    print "Based on heapsort and quicksort times"
    print "%0.2f relative cost for a compare" % ((z1 + z3) / (y1+y3))
    print "%0.2f relative cost for a swap" % ((z1+z4) / (x1+x4))
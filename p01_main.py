__author__ = 'COX1KB'

import mytimer as mt

# Lesson: what is runtime?   runtime ~ cost * O(n)
#   Which would take longer?  Adding 100 pairs of numbers or solving 100 differential equations?
# Which operations run in better time than others?
# Which class is best for run time performance?
# Why does Dr Talaga say "Always use a dictionary and not a list in python"?
# What disadvantage is there to using a dictionary over a list?

#main program
if __name__ == "__main__":

    #let's try different data structures!
    #they will be given the same tests

    mylist = list()
    mydict = dict()
    myset  = set()

    testsize = 10000
    maxrando = 50000
    deletes = 1000

    timer = mt.mytimer()

    #construct full containers
    randomsa = [mt.rando(maxrando) for x in range(0, testsize)]
    randomsb = [mt.rando(maxrando) for x in range(0, testsize)]

    print "\nAppend() operation"
    timer.start()
    for x in range(0,testsize):
        mylist.append( randomsa[x] )
    print "Appending  to list took "+timer.elapsed()

    timer.start()
    for x in range(0,testsize):
        mydict[ randomsa[x]  ] = 1
    print "Appending  to dict took "+timer.elapsed()

    timer.start()
    for x in range(0,testsize):
        myset.add( randomsa[x]  )
    print "Appending  to set  took "+timer.elapsed()


    print "\nContains() operation"
    timer.start()
    for x in randomsb:
        x in mylist  #contains operator
    print "Contains() in list took "+timer.elapsed()

    timer.start()
    for x in randomsb:
        x in mydict #contains operator
    print "Contains() in dict took "+timer.elapsed()

    timer.start()
    for x in randomsb:
        x in myset #contains operator
    print "Contains() in set  took "+timer.elapsed()


    print "\nDelete() operation"
    timer.start()
    for x in range(0,deletes):
        mylist.remove(randomsa[x])
    print "delete()   in list took "+timer.elapsed()

    timer.start()
    for x in range(0,deletes):
        if (randomsa[x] in mydict):  mydict.pop(randomsa[x])
    print "delete()   in dict took "+timer.elapsed()

    timer.start()
    for x in range(0,deletes):
        if (randomsa[x] in myset):  myset.remove(randomsa[x])
    print "delete()   in set  took "+timer.elapsed()

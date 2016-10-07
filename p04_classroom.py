__author__ = 'COX1KB'

# I observed as people came in late to a scientific talk, that manners prevented them from walking to the front row
# to free chairs, instead engaging in absurd behavior.
# Run the simulator.
# What insight did the mysterious stranger have into the data structure?
# Can you find the problem line in the code?  Hint: search for the word "penalty"
# What is particularly stupid about the 'program' the people are running from a programmer's point of view?
# What is the key vocabulary word here?

import mytimer as mt
import classroom as cr

if __name__ == "__main__":

    moves = []
    numPeople = 28

    print "*****\nExciting Scientific Talk simulator v6.1.3"
    print "Where we obey one rule: you can't sit in front of a full row!  We're not barbarians, after all.\n"

    for x in range(0,numPeople):
        moves.append( (mt.rando(4)-1, mt.rando(4)-1) )

    print "\n*****\nLet's simulate seating people\n"
    myclass = cr.classroom()
    time = 0
    for x in range(0,numPeople):
        time += myclass.seatPerson( moves[x] )
    print myclass.toString()
    print "Seating everyone took "+str(time)+" seconds."

    print "\n*****\nNow let's try again, but do things a little differently.  (People sit in same spots)\n"
    myclass = cr.classroom()
    print "Someone yells 'I bet we're gonna have moar peepel dan dis many chairs!'"
    myclass.addSeats(10)
    time = 0
    for x in range(0,numPeople):
        time += myclass.seatPerson( moves[x] )
    print myclass.toString()
    print "Seating everyone took "+str(time)+" seconds."


# YOU CAN'T RUN this code with the files I gave you.

# I want to get line 4862 of the file
# Which command is faster?
#
# head -n 4862 myfile | tail -n 1       Complexity O(2n)
# python p06_bash.py myfile             Complexity O(n)
#
# Why is that so?
# What can we learn about built-in commands from operating system?
#
# A C++ program would be faster.  How would it compare to  head/tail command?

import sys

if __name__ == "__main__":
    k=0
    for line in open(sys.argv[1],'r'):
       k+=1
       if (k == 4862): print line.strip('\n')

    #chopping this up into many lines slows us down
    #we only want line 4862; I can skip the first 4861
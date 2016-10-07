__author__ = 'COX1KB'

class classroom:
    def __init__(self):
        self.rows = [[0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0]]
        self.counts = [0,0,0,0,0,0]
        # self.overflow =
        # self.standing=[0,0]
        self.size = 22
        self.rowlock = -1
        self.oversize = 0
        self.people = 0

    def seatPerson(self, tuple2choice):
        time = 0
        (first, second) = tuple2choice
        if first > self.rowlock:
            if self.isSpaceFree(first):
                time += self.sit(first)
        elif second > self.rowlock:
            if self.isSpaceFree(second):
                time += self.sit(second)
        elif self.rowlock == 5:
            time += 10          #penalty: major disruption and commotion
            print "person "+str(self.people+1)+" causes a disturbance as he knocks over people standing by door, then leaves"
            self.people+=1
        else:
            time += self.sit(self.rowlock+1)
        return time

    def sit(self,row):
        time = 0
        if row < 3:
            for k in range(0,6):
                if self.rows[row][k] == 0:
                    self.rows[row][k] = (self.people+1)
                    print "person "+str(self.people+1)+" sits in row "+str(row)
                    time += 2*(4-row)+3*(k % 4) #penalty: walk from front towards front and down the aisle
                    if k == 5 and self.rowlock < row:
                        self.rowlock = row
                    self.counts[row] += 1
                    break
        elif row == 3:
            for k in range(0,4):
                if self.rows[row][k] == 0:
                    self.rows[row][k] = (self.people+1)
                    print "person "+str(self.people+1)+" sits in row "+str(row)
                    time += 2*(4-row)+3*(k % 4)  #penalty: walk from front towards front and down the aisle
                    if k == 3 and self.rowlock < row:
                        self.rowlock = row
                    self.counts[row] += 1
                    break
        elif row == 4:
            for k in range(0,10):
                if self.rows[row][k] == 0:
                    self.rows[row][k] = (self.people+1)
                    time += k           #penalty: seats are right next to the door, sitting down is fast
                    if k >= self.oversize:
                        print "person "+str(self.people+1)+" finds no seats left"
                        time += self.addSeats(2)
                    if k == 9 and self.rowlock < row:
                        self.rowlock = row
                    self.counts[row] += 1
                    print "person "+str(self.people+1)+" sits in overflow"
                    break
        elif row == 5:
            for k in range(0,2):
                if self.rows[row][k] == 0:
                    #penalty: none; they don't take time to sit!
                    self.rows[row][k] = (self.people+1)
                    print "person "+str(self.people+1)+" stands in standing room only"
                    time += 0
                    self.counts[row] += 1
                    if self.counts[row] == 2: self.rowlock = 5
                    break

        self.people += 1
        return time

    def isFull(self,row):
        result = True
        for k in range(self.rowlock+1,6):
            if self.isSpaceFree(k):
                result = False
                break
        return result

    def isSpaceFree(self,row):
        result = False
        if row < 3 and self.counts[row] < 6:
            result = True
        if row == 3 and self.counts[row] < 4:
            result = True
        if row == 4 and self.counts[row] < self.oversize:
            result = True
        if row == 5 and self.counts[row] < 2 and self.oversize == 10:
            result = True
        return result

    def addSeats(self,number):
        addit = 0
        if (number + self.oversize) <= 10:
            addit = number
        else:
            addit = 10 - self.oversize
        time = self.oversize*addit + 2*addit    #penalty: crowded penalty, disruptive, plus 2 secs per chair
        self.oversize += addit
        self.size += addit
        print "\tSomeone gets out "+str(addit)+" more chairs"
        return time

    def toString(self):
        result = ""
        for k in range(0,4):
            result += "row "+str(k)+" "+str(self.rows[k])+"\n"
        result += "row 4 "+str(self.rows[4][:self.oversize])+"\n"
        result += "stand "+str(self.rows[5])+"\n"
        return result
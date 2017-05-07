import time

mylist = []
with open('list2.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))


startTime = time.clock()
print "Sort Python"
print "Lista nesortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
c = mylist.sort()
print "Lista sortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
print "Numar de elemente in lista:", len(mylist)


endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)
miliseconds,rest = divmod(seconds,60)
print "Timpul de executie: %d hours:%02d minutes:%02d seconds:%02d" % (hours, minutes, seconds,miliseconds)



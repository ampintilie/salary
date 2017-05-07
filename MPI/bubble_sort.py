
import time
mylist = []
with open('list1.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))



def bubbleSort2(x):
    print "Bubble sort"
    print "Lista nesortata:", x[0:21], "......", x[len(mylist) - 20:len(mylist)]
    n = len(x)
    nrc = 0
    nrm = 0
    inter = True
    while inter == True:
        inter = False
        for i in range(0, n - 1):
            nrc = nrc + 1
            if x[i] > x[i + 1]:
                aux = x[i]
                x[i] = x[i + 1]
                x[i + 1] = aux
                nrm = nrm + 3
                inter = True
    print "Lista sortata:", x[0:21], "......", x[len(mylist) - 20:len(mylist)]
    print "Numar de elemente in lista:",len(mylist)
    print "Numar de comparari = ","{:,}".format(nrc)
    print "Numar de mutari elemente in sir = ", "{:,}".format(nrm)
    return x


startTime = time.clock()
bubbleSort2(mylist)
endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)

print "Timpul de executie: %d hours:%02d minutes:%02d seconds" % (hours, minutes, seconds)



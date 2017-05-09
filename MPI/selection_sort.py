import time

mylist = []
with open('list1.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))


def selectionSort(a):
    print "Selection sort"
    print "Lista nesortata:", a[0:21], "......", a[len(a) - 20:len(a)]
    nrc = 0
    nrm = 0
    for i in range(0,len(a)):
        min = i
        for j in range(i + 1, len(a)):
            nrc = nrc + 1
            if a[j] < a[min]:
                min = j
        aux = a[i]
        a[i] = a[min]
        a[min] = aux
        nrm = nrm + 3
    print "Lista sortata:", a[0:21], "......", a[len(a) - 20:len(a)]
    print "Numar de elemente in lista:", len(a)
    print "Numar de comparari = ", "{:,}".format(nrc)
    print "Numar de mutari elemente in sir = ", "{:,}".format(nrm)
    return a


startTime = time.clock()
selectionSort(mylist)
endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)
print "Timpul de executie: %d hours:%02d minutes:%02d seconds" % (hours, minutes, seconds)






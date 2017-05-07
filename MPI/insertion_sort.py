import time

mylist = []
with open('list1.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))


def sortareInsertie(a):
    print "Insertion Sort"
    print "Lista nesortata:", a[0:21], "......", a[len(a) - 20:len(a)]
    nrc = 0
    nrm = 0
    n = len(a)
    j = 0
    for i in range (1,n):
        aux = a[i]
        nrm += 1
        j = i - 1
        while j >= 0 and aux < a[j]:
            nrc += 1
            a[j + 1] = a[j]
            nrm += 1
            j -= 1
        nrc += 1
        a[j+1] = aux
        nrm += 1
    print "Lista sortata:", a[0:21], "......", a[len(a) - 20:len(a)]
    print "Numar de elemente in lista:", len(a)
    print "Numar de comparari = ", "{:,}".format(nrc)
    print "Numar de mutari elemente in sir = ", "{:,}".format(nrm)
    return a


startTime = time.clock()
sortareInsertie(mylist)
endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)
print "Timpul de executie: %d hours:%02d minutes:%02d seconds" % (hours, minutes, seconds)



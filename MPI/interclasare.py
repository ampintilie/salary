import time

mylist = []
with open('list1.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))

def interclasare(x, s, d, m, nrc):
    i = s
    j = m + 1
    k = 0
    nrc += 1
    c = [0] * (d - s + 1)
    while i <= m and j <= d:
        nrc += 1
        if x[i] <= x[j]:
            c[k] = x[i]
            i += 1
        else:
            c[k] = x[j]
            j += 1
        k += 1
    nrc += 1
    while i <= m:
        c[k] = x[i]
        i += 1
        k += 1
        nrc += 1
    nrc += 1
    while j <= d:
        nrc += 1
        c[k] = x[j]
        k += 1
        j += 1
    for i in range(s, d + 1):
        x[i] = c[i - s]
    return nrc

def mergesort(x, s, d, nrc):
    nrc += 1
    if s < d:
        m = (s + d) / 2
        nrc = mergesort(x, s, m, nrc)
        nrc = mergesort(x, m + 1, d, nrc)
        nrc = interclasare(x, s, d, m, nrc)
    return nrc


startTime = time.clock()
print "MergeSort(Interclasare)"
print "Lista nesortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
c = mergesort(mylist,0,len(mylist)-1,0)
print "Lista sortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
print "Numar de elemente in lista:", len(mylist)
print "Numar de comparari = ", "{:,}".format(c)

endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)
miliseconds,rest = divmod(seconds,60)
print "Timpul de executie: %d hours:%02d minutes:%02d seconds:%02d" % (hours, minutes, seconds,miliseconds)







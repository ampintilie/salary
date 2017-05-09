
import time
mylist = []
with open('list1.txt') as f:
    for line in f:
        numbers = line.split()
        for i in numbers:
            mylist.append(int(i))


def partitie(x,s,d,nrc):
    v=x[s]
    i=s-1
    j=d+1
    while i<j:
        nrc +=1
        i += 1
        while x[i]<v:
            i +=1
            nrc +=1
        nrc+=1
        j -= 1
        while x[j]>v:
            j-=1
            nrc+=1
        nrc+=1
        if i<j :
            x[i],x[j]=x[j],x[i]
    return j,nrc

def quicksort(x,s,d,nrc):
    nrc = nrc +1
    if (s<d):
        q,nrc=partitie(x,s,d,nrc)
        nrc=quicksort(x,s,q,nrc)
        nrc=quicksort(x,q+1,d,nrc)
    return nrc



startTime = time.clock()
print "QuickSort"
print "Lista nesortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
c = quicksort(mylist,0,len(mylist)-1,0)
print "Lista sortata:", mylist[0:21], "......", mylist[len(mylist) - 20:len(mylist)]
print "Numar de elemente in lista:", len(mylist)
print "Numar de comparari = ", "{:,}".format(c)

endTime = time.clock()

timeTaken = endTime - startTime
hours, rest = divmod(timeTaken,3600)
minutes,seconds = divmod(rest,60)
miliseconds,rest = divmod(seconds,60)
print "Timpul de executie: %d hours:%02d minutes:%02d seconds:%02d" % (hours, minutes, seconds,miliseconds)




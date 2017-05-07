import random


mylist1 = []            # elemente random
for i in range(10000):
    i = random.randrange(1,10000)
    mylist1.append(i)
with open('list1.txt', 'w') as f:
    for i in mylist1:
        f.write("%d " %i)
    f.close()


mylist2 = []               # elemente random
for i in range(500000):
    i = random.randrange(1,5000000)
    mylist2.append(i)
with open('list2.txt', 'w') as f:
    for i in mylist2:
        f.write("%d " %i)
    f.close()


mylist3 = []                # elemente random
for i in range(5000000):
    i = random.randrange(1,50000000)
    mylist3.append(i)
with open('list3.txt', 'w') as f:
    for i in mylist3:
        f.write("%d " %i)
    f.close()


mylist4 = []                # elemente random
for i in range(20000000):
    i = random.randrange(1,200000000)
    mylist4.append(i)
with open('list4.txt', 'w') as f:
    for i in mylist4:
        f.write("%d " %i)
    f.close()


mylist5 = []                # lista ordonata crescator
for i in range(200000):
    i = random.randrange(1,2000000)
    mylist5.append(i)
mylist5.sort()
with open('list5.txt', 'w') as f:
    for i in mylist5:
        f.write("%d " %i)
    f.close()


mylist6 = []      # lista ordonata descrescator
for i in range(5000000):
    i = random.randrange(1,50000000)
    mylist6.append(i)
mylist6.sort(reverse=True)
with open('list6.txt', 'w') as f:
    for i in mylist6:
        f.write("%d " %i)
    f.close()


mylist7 = []        # lista ordonata crescator avand doar cateva elemente care nu sunt la locul lor
for i in range(1,5000000):
    if i % 10000 == 0:
        for j in range(2):
            j = random.randrange(100,200)
            mylist7.append(j)
    else:
        mylist7.append(i)
with open('list7.txt', 'w') as f:
    for i in mylist7:
        f.write("%d " %i)
    f.close()
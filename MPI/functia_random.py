import random

mylist1 = []  # elemente random 10.000
for i in range(10000):
    i = random.randrange(1, 10000)
    mylist1.append(i)
with open('list1.txt', 'w') as f:
    for i in mylist1:
        f.write("%d " % i)
    f.close()

mylist2 = []  # elemente random 200.000
for i in range(200000):
    i = random.randrange(1, 2000000)
    mylist2.append(i)
with open('list2.txt', 'w') as f:
    for i in mylist2:
        f.write("%d " % i)
    f.close()

mylist3 = []  # elemente random 500.000
for i in range(500000):
    i = random.randrange(1, 5000000)
    mylist3.append(i)
with open('list3.txt', 'w') as f:
    for i in mylist3:
        f.write("%d " % i)
    f.close()

mylist4 = []  # elemente random 5.000.000
for i in range(5000000):
    i = random.randrange(1, 50000000)
    mylist4.append(i)
with open('list4.txt', 'w') as f:
    for i in mylist4:
        f.write("%d " % i)
    f.close()

mylist5 = []  # elemente random 20.000.000
for i in range(20000000):
    i = random.randrange(1, 200000000)
    mylist5.append(i)
with open('list5.txt', 'w') as f:
    for i in mylist5:
        f.write("%d " % i)
    f.close()

mylist6 = []  # elemente random 200.000.000
for i in range(200000000):
    i = random.randrange(1, 2000000000)
    mylist6.append(i)
with open('list6.txt', 'w') as f:
    for i in mylist6:
        f.write("%d " % i)
    f.close()

mylist7 = []  # lista ordonata crescator
for i in range(200000):
    i = random.randrange(1, 2000000)
    mylist7.append(i)
mylist7.sort()
with open('list7.txt', 'w') as f:
    for i in mylist7:
        f.write("%d " % i)
    f.close()

mylist8 = []  # lista ordonata descrescator cu 200.000 elemente
for i in range(200000):
    i = random.randrange(1, 2000000)
    mylist8.append(i)
mylist8.sort(reverse=True)
with open('list8.txt', 'w') as f:
    for i in mylist8:
        f.write("%d " % i)
    f.close()

mylist9 = []  # lista ordonata crescator avand doar cateva elemente care nu sunt la locul lor cu 200.000 elemente
for i in range(1, 200000):
    if i % 10000 == 0:
        for j in range(2):
            j = random.randrange(100, 200)
            mylist9.append(j)
    else:
        mylist9.append(i)
with open('list9.txt', 'w') as f:
    for i in mylist9:
        f.write("%d " % i)
    f.close()



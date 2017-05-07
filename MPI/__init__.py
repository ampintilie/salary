import random

mylist7 = []        # lista ordonata crescator avand doar cateva elemente care nu sunt la locul lor
for i in range(1,200000):
    if i % 10000 == 0:
        for j in range(4):
            j = random.randrange(100,200)
            mylist7.append(j)
    else:
        mylist7.append(i)
print mylist7

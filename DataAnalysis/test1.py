import numpy
import random
import matplotlib.pyplot

def fib(n):
    a=1
    b=1
    while(True):
        yield a
        a,b=b,a+b
        if(n==1):
            break
        n-=1

'''g=fib(10)
s=0
while(True):
    try:
        j=next(g)
        print(j)
        s+=j
    except StopIteration:
        break
print("end".center(50,"-"))
print("{na}".format(na=s))'''


f=matplotlib.pyplot.figure()


ax1=matplotlib.pyplot.subplot2grid((3,3),(0,0),colspan=2,rowspan=1)
a=list(range(1,6,1))
b=[random.randint(5,15) for i in range(5)]
ax1.bar(a,b,color="#ff0000")


matplotlib.pyplot.show()

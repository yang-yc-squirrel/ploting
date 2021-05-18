import operator
import numpy
def select(x):
    new_x=[]
    while(True):
        mi=x[0]
        ci=0
        for i in range(len(x)):
            if(operator.lt(x[i],mi)):
                mi=x[i]
                ci=i
        new_x.append(mi)
        x.remove(x[ci])
        if(len(x)==1):
            new_x.extend(x)
            break
    return new_x

a=numpy.random.randint(2,12,size=(6,3))

a=list(a.flatten())
print(a)
a=select(a)
print(a)
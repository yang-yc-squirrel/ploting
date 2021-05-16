import random
def buddle(x):
    l=len(x)
    while(l>=2):
        for i in range(0,l-1,1):
            if(x[i]>x[i+1]):
                x[i],x[i+1]=x[i+1],x[i]
        l-=1
    return x

x=[6,7,3,5,22,0,76,3,55,11,0,3,7,5,88]
print(buddle(x))
import operator
import numpy
import matplotlib.pyplot

def conflict(pos):
    res=False
    flag=0
    for i in range(0,len(pos)-1,1):
        for j in range(i+1,len(pos),1):
            if(operator.eq(pos[i],pos[j]) or operator.eq(abs(i-j),abs(pos[i]-pos[j]))):
                res=True
                flag=1
                break
        if(operator.eq(flag,1)):
            flag=0
            break

    return res

def initpos(n):
    pos=[0 for i in range(n)]
    return pos




solnums=0
solindex=[]
n=8
pos=initpos(n)
k=1
flag=0
while(True):
    while(True):

        if(operator.ge(pos[k],n)):
            pos[k]=0
            k-=1
            if(operator.eq(k,0)):
                pos[0]+=1
                k=1
            else:
                pos[k] += 1
        if (conflict(pos[0:k + 1:1])):
            pos[k] += 1
            if (operator.ge(pos[k], n)):
                pos[k] = 0
                k -= 1
                if (operator.eq(k, 0)):
                    pos[0] += 1
                    if(operator.ge(pos[0],n)):
                        break
                    k = 1
                else:
                    pos[k] += 1
        else:
            break

    k=k+1
    if (operator.ge(pos[0], n)):
        flag = 1

    if(operator.ge(k,n)):
        solnums+=1
        solindex.append(pos.copy())
        k-=1
        pos[k]+=1
    if(operator.eq(flag,1)):
        flag=0
        break

print("when the number of pieces is {s1} the number of solutions is {s2}".format(s1=n,s2=solnums))

f=matplotlib.pyplot.figure()
matplotlib.pyplot.axis([-1,n+1,-1,n+1])
matplotlib.pyplot.axis("off")

counts=0
while(True):
    matplotlib.pyplot.cla()
    for i in range(n + 1):
        x1 = numpy.ones(shape=(1, 500)).flatten() * i
        y1 = numpy.linspace(0, n, 500)
        matplotlib.pyplot.plot(x1, y1, color=(1, 0, 0))
        x2 = numpy.linspace(0, n, 500)
        y2 = numpy.ones(shape=(1, 500)).flatten() * i
        matplotlib.pyplot.plot(x2, y2, color=(1, 0, 0))
        matplotlib.pyplot.axis("off")

    qy = numpy.array([i + 0.5 for i in range(n)])
    qx = numpy.array(solindex[counts]) + 0.5
    matplotlib.pyplot.scatter(qx, qy, color=(0, 0, 1), s=25, alpha=0.6)
    counts+=1
    matplotlib.pyplot.pause(0.5)
    if(operator.ge(counts,solnums)):
        counts=0
        break



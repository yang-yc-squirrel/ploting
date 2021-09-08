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

ax2=matplotlib.pyplot.subplot2grid((3,3),(0,2),colspan=1,rowspan=2)
x=numpy.linspace(0,2*numpy.pi,100)
y=numpy.zeros(shape=(1,100)).flatten()
for i in range(100):
    y[i]=numpy.sin(2*x[i])
ax2.plot(x,y,color="#ff0000")
matplotlib.pyplot.tight_layout()

ax3=matplotlib.pyplot.subplot2grid((3,3),(1,1),colspan=1,rowspan=1,projection="polar")
th=numpy.arange(0,numpy.pi,numpy.pi/6)
r=numpy.array([random.randint(1,6) for i in range(6)])
ws=[random.randint(2,5)*numpy.pi/30 for i in range(6)]
ax3.bar(th,r,width=ws)
ax3.set_rlim([0,10])
ax3.set_rticks(numpy.arange(0,3,0.1))
ax3.set_rlabel_position(300)

ax4=matplotlib.pyplot.subplot2grid((3,3),(1,0),colspan=1,rowspan=2)
ax4.bar([2,4,6],numpy.random.randint(5,10,size=(1,3)).flatten(),width=0.5,facecolor=(1,0.5,0))
matplotlib.pyplot.xticks([2,4,6],list("abc"))
xt=ax4.get_xticklabels()
[n.set_fontname("Times New Roman") for n in xt]
yt=ax4.get_yticklabels()
[n.set_fontname("Times New Roman") for n in yt]
matplotlib.pyplot.tick_params(labelsize=16)


matplotlib.pyplot.show()

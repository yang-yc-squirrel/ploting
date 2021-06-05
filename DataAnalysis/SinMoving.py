import numpy
import random
import matplotlib.pyplot
import matplotlib.animation


f=matplotlib.pyplot.figure()
ax=matplotlib.pyplot.axes(xlim=(0,2*numpy.pi),ylim=(-1.5,1.5))
b,=ax.plot([],[])
x=[]
y=[]
def init():
    b.set_data(x,y)
    return b,

def newf(i):
    x.append(i)
    y.append(numpy.sin(i))
    b.set_data(x,y)
    return b,

m=matplotlib.animation.FuncAnimation(f,newf,frames=numpy.linspace(0,2*numpy.pi,100),init_func=init,interval=3,blit=True)
matplotlib.pyplot.show()

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
    x=numpy.linspace(0,i,300)
    y=numpy.sin(x)
    b.set_data(x,y)
    return b,

m=matplotlib.animation.FuncAnimation(f,newf,frames=numpy.linspace(0,2*numpy.pi,100),init_func=init,blit=True,interval=30)
matplotlib.pyplot.show()

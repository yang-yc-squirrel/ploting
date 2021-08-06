import numpy
import matplotlib.pyplot
import matplotlib.animation

def cauchy(x,t,s):
    fx=s*numpy.pi*(1+((x-t)/s)**2)
    fx=1/fx
    return fx

def Gaussian(x,u,s):
    fx=numpy.exp(-1*((x-u)**2)/(2*(s**2)))
    fx=fx/s*((2*numpy.pi)**0.5)
    return fx

p=matplotlib.pyplot.figure()
ax=matplotlib.pyplot.axes(xlim=(-10,10),ylim=(0,1))
f,=ax.plot([],[])
x=[]
y=[]

def init():
    f.set_data(x,y)
    return f,

def upd(t):
    x=numpy.linspace(-10,10,1000)
    y=numpy.zeros(shape=(1,1000)).flatten()
    for i in range(1000):
        y[i]=cauchy(x[i],0,t)
    f.set_data(x,y)
    return f,

m=matplotlib.animation.FuncAnimation(p,upd,frames=numpy.linspace(0.5,5,300),init_func=init,blit=True,interval=30)
matplotlib.pyplot.show()
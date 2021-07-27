import numpy
import matplotlib.pyplot
import matplotlib.animation

def cauchy(x,t,s):
    fx=s*numpy.pi*(1+((x-t)/s)**2)
    fx=1/fx
    return fx

p=matplotlib.pyplot.figure()
ax=matplotlib.pyplot.axes(xlim=(-10,10),ylim=(0,1))
f,=ax.plot([],[])
x=[]
y=[]
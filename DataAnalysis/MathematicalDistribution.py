import numpy
import matplotlib.pyplot

def cauchy(x,t,s):
    fx=s*numpy.pi*(1+((x-t)/s)**2)
    fx=1/fx
    return fx

x=numpy.linspace(-10,10,1000)
fx=numpy.zeros(shape=(1,1000)).flatten()
for i in range(1000):
    fx[i]=cauchy(x[i],0,1)

p=matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x,fx,label="f(x)=cauchy(x)")
matplotlib.pyplot.legend(loc=1)
matplotlib.pyplot.show()
import matplotlib.pyplot
import numpy

def f(x):
    c=10
    return c if x<=c else x

x=numpy.linspace(0,20,200)
y=numpy.zeros(shape=(1,200)).flatten()
for i in range(200):
    y[i]=f(x[i])

p=matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x,y,label="function")
matplotlib.pyplot.legend(loc=2)
matplotlib.pyplot.show()
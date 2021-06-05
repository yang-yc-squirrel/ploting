import numpy
import matplotlib.pyplot
import matplotlib.animation


f=matplotlib.pyplot.figure()
x=numpy.linspace(0,2*numpy.pi,500)
y=numpy.zeros(shape=(1,500)).flatten()
for i in range(500):
    y[i]=numpy.sin(x[i])
a=f.gca()
a.plot(x,y,label="y$_1$=sin(x)")
matplotlib.pyplot.legend(loc=1)
matplotlib.pyplot.xlabel("time",fontdict={"family":"Times New Roman","size":20})
matplotlib.pyplot.annotate("y=sin(1)",xy=(1,0.3),xytext=(1,0.6),arrowprops=dict(facecolor='black', shrink=0.05))
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

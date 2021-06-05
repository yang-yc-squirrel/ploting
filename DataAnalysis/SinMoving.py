import numpy
import matplotlib.pyplot
import matplotlib.animation


f=matplotlib.pyplot.figure()
ax=f.gca(projection="polar")
ax.bar(numpy.pi,3,width=numpy.pi/3)
matplotlib.pyplot.show()
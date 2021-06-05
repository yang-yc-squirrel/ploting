import numpy
import random
import matplotlib.pyplot
import matplotlib.animation


f=matplotlib.pyplot.figure()
x=numpy.random.randint(1,9,size=(3,50)).flatten()
y=numpy.random.randint(1,9,size=(50,3)).flatten()
matplotlib.pyplot.axis([0,10,0,10])
for i in range(len(x)):
    sizes=random.randint(10,30)
    matplotlib.pyplot.scatter(x[i],y[i],s=sizes,color="#ff0000",alpha=0.3)

matplotlib.pyplot.annotate("scatter",xy=(5,5),xytext=(7,5),arrowprops={"facecolor":"blue","shrink":0.08})
matplotlib.pyplot.show()

import numpy
import random
import matplotlib.pyplot
import matplotlib.animation
import pywt

x=numpy.linspace(0,1,1024)
y=numpy.zeros(shape=(1,1024)).flatten()
for i in range(1024):
    y[i]=10*numpy.cos(2*numpy.pi*50*x[i])+15*numpy.sin(2*numpy.pi*20*x[i])


maxi,mini=numpy.argsort(y)[0],numpy.argsort(y)[-1]
ymax=y[maxi]
ymin=y[mini]

y_new=[]
for i in range(1024):
    res=((y[i]-ymax)+(y[i]-ymin))/(ymax-ymin)
    y_new.append(res)
y_new=numpy.array(y_new)
x_new=x/1024

r=x_new.copy()
th=[]
for i in range(1024):
    th.append(numpy.arccos(y_new[i]))
th=numpy.array(th)

G=numpy.zeros(shape=(1024,1024))
for i in range(1024):
    for j in range(1024):
        G[i,j]=numpy.cos(th[i]+th[j])


f=matplotlib.pyplot.figure()
f1=f.add_subplot(1,3,1)
matplotlib.pyplot.sca(f1)
matplotlib.pyplot.plot(x,y)
f2=f.add_subplot(1,3,2,projection="polar")
matplotlib.pyplot.sca(f2)
f2.plot(th,r,color=(1,0,0))
matplotlib.pyplot.show()
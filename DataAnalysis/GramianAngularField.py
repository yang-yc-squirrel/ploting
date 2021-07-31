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
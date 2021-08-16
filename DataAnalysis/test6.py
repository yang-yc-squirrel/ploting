import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os
import collections
import docx
import turtle
import heapq
import re
import operator
import cv2
from PIL import Image

def fx(x):
    y=10*numpy.sin(100*numpy.pi*x)+15*numpy.sin(50*numpy.pi*x)+25*numpy.cos(20*numpy.pi*x)+2*numpy.sin(5*numpy.pi*x)+15*numpy.cos(80*numpy.pi*x)
    return y

x=numpy.linspace(0,1,1024)
y=numpy.zeros(shape=(1,1024)).flatten()

for i in range(1024):
    y[i]=fx(x[i])

f=matplotlib.pyplot.figure()
f1=f.add_subplot(2,1,1)
f2=f.add_subplot(2,2,3,projection="polar")
f3=f.add_subplot(2,2,4)
matplotlib.pyplot.sca(f1)
matplotlib.pyplot.plot(x,y,color=(1,0,1),label="y$_1$=signal(x)")
matplotlib.pyplot.legend(loc=5)
matplotlib.pyplot.xlabel("signal",fontdict={"family":"Times New Roman","size":20})
matplotlib.pyplot.tick_params(labelsize=10)

ysi=numpy.argsort(y)

ymax=y[ysi[-1]]
ymin=y[ysi[0]]
y_new=numpy.zeros(shape=(1,1024)).flatten()
for i in range(1024):
    y_new[i]=((y[i]-ymax)+(y[i]-ymin))/(ymax-ymin)
th=numpy.zeros(shape=(1,1024)).flatten()
for i in range(1024):
    th[i]=numpy.arccos(y_new[i])

r=numpy.array([x[i]/1024 for i in range(1024)])
matplotlib.pyplot.sca(f2)
f2.scatter(th,r,s=3,color=(1,0,0),alpha=0.5)
f2.set_rlim(0,0.001)
matplotlib.pyplot.tick_params(labelsize=10)



G=numpy.zeros(shape=(1024,1024))
for i in range(1024):
    for j in range(1024):
        G[i,j]=numpy.cos(th[i]+th[j])
matplotlib.pyplot.sca(f3)
matplotlib.pyplot.imshow(G,cmap=matplotlib.pyplot.get_cmap("winter"))
matplotlib.pyplot.tick_params(labelsize=10)
matplotlib.pyplot.show()

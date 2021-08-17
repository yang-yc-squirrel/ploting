import matplotlib.pyplot
import mpl_toolkits.mplot3d
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
    y=10*numpy.sin(100*numpy.pi*x)+15*numpy.sin(50*numpy.pi*x)
    z=25*numpy.cos(20*numpy.pi*x)+2*numpy.sin(5*numpy.pi*x)+15*numpy.cos(80*numpy.pi*x)
    return y,z

x=numpy.linspace(0,1,1024)
y=numpy.zeros(shape=(1,1024)).flatten()
z=numpy.zeros(shape=(1,1024)).flatten()

for i in range(1024):
    y[i],z[i]=fx(x[i])

f=matplotlib.pyplot.figure()
f3d=mpl_toolkits.mplot3d.Axes3D(f)

a=0
f3d.plot(x,y,z,color=(1,0,0))
for i in range(0,90,10):
    f3d.view_init(i,20)
    matplotlib.pyplot.show()


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




G=numpy.zeros(shape=(1024,1024))
for i in range(1024):
    for j in range(1024):
        G[i,j]=numpy.cos(th[i]+th[j])



#matplotlib.pyplot.show()
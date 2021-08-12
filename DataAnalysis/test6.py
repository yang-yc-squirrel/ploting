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
    d=len(x)
    s=0
    for i in range(d):
        s+=((x[i]**2)-10*numpy.cos(2*numpy.pi*x[i]))
    s+=10*d
    return s

a=list(range(16))
print(a)
c1=list(itertools.combinations(a,3))
print(len(c1))

f=matplotlib.pyplot.figure()
f1=f.add_subplot(1,2,1,projection="polar")
matplotlib.pyplot.sca(f1)
t=numpy.arange(0,numpy.pi,numpy.pi/6)
r=numpy.array([random.uniform(0.5,5) for i in range(6)])
f1.scatter(t,r,color=(1,0,0),s=numpy.array([random.choice(list(range(30,90,10))) for i in range(6)]),alpha=0.2)

f2=f.add_subplot(1,2,2,projection="3d")
matplotlib.pyplot.sca(f2)
o=numpy.linspace(-5,5,100)
p=numpy.linspace(-5,5,100)
x,y=numpy.meshgrid(o,p)
z=numpy.zeros(shape=(100,100))
for i in range(100):
    for j in range(100):
        z[i,j]=fx([x[i,j],y[i,j]])
f2.plot_surface(x,y,z,cmap=matplotlib.pyplot.get_cmap("winter"))
matplotlib.pyplot.show()




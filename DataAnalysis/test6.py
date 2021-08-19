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


def F(x):
    d=len(x)
    s=0
    for i in range(d):
        s+=x[i]*numpy.sin((abs(x[i]))**0.5)
    s=s*(-1)+418.9829*d
    return s

p=numpy.linspace(0,200,1000)

x,y=numpy.meshgrid(p,p)
z=numpy.zeros(shape=(1000,1000))
for i in range(1000):
    for j in range(1000):
        z[i,j]=F([x[i,j],y[i,j]])

f=matplotlib.pyplot.figure()
fn=mpl_toolkits.mplot3d.Axes3D(f)
#fn.plot_surface(x,y,z,cmap=matplotlib.pyplot.get_cmap("hot"))
fn.contourf(x,y,z,cmap=matplotlib.pyplot.get_cmap("hot"))
matplotlib.pyplot.savefig("F:/ff.jpg")

a=cv2.imread("F:/ff.jpg")
print(a)
a1=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("f",a1)
cv2.waitKey(0)
cv2.destroyAllWindows()

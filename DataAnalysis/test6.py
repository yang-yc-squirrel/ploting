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

f3d.scatter3D(x,y,z,color="#ff0000",alpha=0.5)

p=cv2.imread("F:/figure.jpg")
p1=cv2.pyrDown(p)
p2=cv2.pyrDown(p1)

cv2.imshow("p",p)
cv2.imshow("p1",p1)
cv2.imshow("p2",p2)

cv2.waitKey(0)
cv2.destroyAllWindows()
print(p1)
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
matplotlib.pyplot.show()


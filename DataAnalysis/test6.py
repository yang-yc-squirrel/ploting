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

p=numpy.linspace(0,500,2000)
print(p)
x,y=numpy.meshgrid(p,p)
print(x)

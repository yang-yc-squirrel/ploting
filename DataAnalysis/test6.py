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

x=numpy.linspace(0,2*numpy.pi,1024)
y=numpy.zeros(shape=(1,1024)).flatten()
print(x)
print(y)




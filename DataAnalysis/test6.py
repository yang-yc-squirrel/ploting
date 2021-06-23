import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os

a=numpy.random.randint(0,10,size=(1,15)).flatten()
print(a)
b=numpy.argsort(a)
print(b)
b1=list(b)
print(b1)
b2=numpy.array(b1)
print(b2)
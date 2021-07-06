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

a=numpy.array([random.choice(list(range(50))) for i in range(30)])
a=a.reshape(5,6)
print(a)
p=pandas.DataFrame(a)
print(p)
p=p.set_index([1],drop=True)
print(p)
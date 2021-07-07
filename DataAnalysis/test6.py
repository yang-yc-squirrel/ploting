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


a=list(range(20))
print(a)
a_new=list(map(lambda x:2*x-25,a))
print(a_new)
s=numpy.array([random.choice(a_new) for _ in range(45)]).reshape(-1,5)
print(s)
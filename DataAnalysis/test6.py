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
s=numpy.array([random.choice(a_new) for _ in range(15)]).reshape(-1,5)
print(s)
d=pandas.DataFrame(s,columns=[chr(ord("a")+i) for i in range(5,10,1)],index=list(range(12,15,1)))
print(d)

z=dict(zip([chr(ord("a")+i) for i in range(5,10,1)],[random.randint(100,200) for _ in range(5)]))
d=d.append([z],ignore_index=True)
print(d)


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


p=numpy.linspace(0,10,24)
print(p)
p=p.reshape(8,-1)
print(p)
o=pandas.DataFrame(p,columns=list("abc"),index=[random.choice([chr(ord("a")+i) for i in range(26)]) for _ in range(8)])
print(o)

a=list(o.iloc[:,0])
print(a)
b=[random.randint(0,20) for i in range(len(a))]
print(b)
b.append(100)
print(b)
df=dict(itertools.zip_longest(b,a,fillvalue="k"))
print(df)
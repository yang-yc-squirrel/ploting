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

a=numpy.array([random.choice(list(range(3))) for i in range(20)])
print(a)
d=dict(collections.Counter(a))
print(d)
nz=len(a)-d.get(0)
print(nz)
ra=nz/len(a)
ra=format(ra,"0.6%")
print(ra)

for i in itertools.dropwhile(lambda x:x==1 or x==2,a):
    print(i,end=" ")

g=list(range(10))
print("\n")
print(g)

def sq(x):
    res=x**2-3*x
    return res

s1=list(map(sq,g))
print(s1)
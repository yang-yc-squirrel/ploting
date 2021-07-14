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

a=numpy.random.randint(5,20,size=(5,3)).flatten()

for x,y in enumerate(a,5):
    di = dict(xx=x, yy=y)
    print("{xx}-{yy}".format(**di))

h=numpy.argsort(a)
print(h)

s=[chr(ord("a")+random.randint(0,25)) for i in range(30)]
print(s)
s="a".join(s)+"ddd"
print(s)
s=s.replace("a","k",3)
print(s)
t=re.split(r"[a]",s)
print(t)

u=[random.choice(list(range(3))) for _ in range(15)]
print(u)
un=[-1 if i==0 else i for i in u]
print(un)
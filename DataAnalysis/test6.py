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
import heapq

a=collections.deque(maxlen=10)
for i in range(20):
    a.appendleft(i)
print(a)

b=[random.randint(0,20) for i in range(10)]
print(b)

heapq.heapify(b)
print(b)
c=heapq.heapreplace(b,100)
print(c)
print(b)
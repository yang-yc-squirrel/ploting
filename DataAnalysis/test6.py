import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os
import collections

b=random.sample(list(range(10,1,-1)),5)
a=numpy.array([random.choice(list(range(3))) for i in range(20)])
print(a)
print(b)
d=dict(collections.Counter(a))
print(d)
fau=len(a)-d.get(0)
print(fau)
ras=fau/len(a)
print(ras)
ras=format(ras,"0.5%")
print("{0:->20}".format("new"))
print(ras)
print(type(ras))
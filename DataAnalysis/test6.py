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
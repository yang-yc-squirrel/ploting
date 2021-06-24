import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os
import collections

a=numpy.array([random.choice(list(range(3))) for i in range(15)])
print(a)
d=dict(collections.Counter(a))
print(d)
fau=len(a)-d.get(0)
print("{fau}".format(fau=fau))
import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os

a=numpy.random.randint(0,10,size=(5,3))
print(a)
print(a.sum(axis=0))
p=pandas.DataFrame(a,columns=list("abc"),index=list(range(5,10,1)))
print(p)
p=p.sort_values(axis=0,by="b")
print(p)
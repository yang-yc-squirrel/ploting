import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools

a=[random.randint(0,10) for i in range(10)]
print(a)
for i in itertools.dropwhile(lambda x:x>3,a):
    print(i)
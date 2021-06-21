import matplotlib.pyplot
import numpy
import pandas
import random
import functools

a=[random.randint(0,15) for i in range(10)]
print(a)
b=functools.reduce(lambda x,y:x+y,a)
print(b)


s=0
for i in a:
    s+=i
print("{0}".format(s))
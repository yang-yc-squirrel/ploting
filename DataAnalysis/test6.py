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
o.to_csv("F:/o.csv",encoding="utf-8",header=0,index=0)
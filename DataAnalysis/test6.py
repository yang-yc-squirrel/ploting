import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools
import json
import os

a="suv"
b=[random.randint(3,10) for i in range(6)]
c=[chr(ord("a")+i) for i in range(8)]
d=dict(a=a,b=b,c=c)
p="F:/test.json"
with open(p,"w") as f:
    json.dump(d,f)
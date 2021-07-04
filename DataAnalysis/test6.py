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

n=eval(input("please inputy a number:"))
di=[9]
i=1
while(i<=10):
    di=di*i
    dis=[str(j) for j in di]
    divs="".join(dis)
    div=eval(divs)
    i+=1

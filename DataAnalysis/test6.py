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


def fei(n):
    a=1
    b=1
    i=1
    while(i<=n):
        yield a
        a,b=b,a+b
        i+=1


g=fei(21)
r=[]
while(True):
    try:
        new_e=next(g)
        r.append(new_e)
    except StopIteration:
        print("end".center(20,"-"))
        break
print(r)



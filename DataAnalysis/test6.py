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

r=numpy.array(r).reshape(-1,3)
print(r)
jk=r.sum(axis=0).reshape(-1,3)
print(jk)
r=numpy.r_[r,jk]
print(format("sum","+>30"))
print(r)
p=pandas.DataFrame(r,columns=[chr(ord("a")+i) for i in range(3)])
print(p)
print("{0:*<30}".format("next"))
p=p.set_index(["b"],drop=True)
print(p)

tx=list(p.iloc[:,0])
print(tx)
print("\n")
for i,j in enumerate(tx,5):
    print("{i} {j}".format(i=i,j=j))

for k in itertools.dropwhile(lambda x:x<200,tx):
    print(k)
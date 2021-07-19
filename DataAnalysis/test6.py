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
import re
from PIL import Image

a=numpy.random.randint(5,20,size=(5,3)).flatten()

for x,y in enumerate(a,5):
    di = dict(xx=x, yy=y)
    print("{xx}-{yy}".format(**di))

h=numpy.argsort(a)
print(h)

s=[chr(ord("a")+random.randint(0,25)) for i in range(30)]
print(s)
s="a".join(s)+"ddd"
print(s)
s=s.replace("a","k",3)
print(s)
t=re.split(r"[a]",s)
print(t)

u=[random.choice(list(range(3))) for _ in range(15)]
print(u)
un=[-1 if i==0 else i for i in u]
print(un)

sr=[chr(ord(random.choice(["a","0"]))+random.randint(0,25)) for _ in range(30)]
print(sr)
ssr="".join(sr)
print(ssr)
me=re.compile("\d+")
tsr=re.sub(me,"%%",ssr)
print(tsr)


print("sss".ljust(50,"-"))

df=[chr(ord("a")+random.choice(list(range(25)))) for _ in range(25)]
print(df)
sf=""
for i in df:
    sf=sf+chr(ord("a")+random.randint(0,25))+i
print(sf)
print(len(sf))
nh=re.compile("[a-f]+")
op=re.findall(nh,sf)
print(op)


a=numpy.array([random.choice(list(range(100))) for _ in range(75)]).reshape(-1,3)
print(a)
pa=pandas.DataFrame(a,columns=list("abc"))
print(pa)
pa1=pa.sample(n=10,replace=True)
print(pa1)

pa2=pa.sample(frac=0.1)
print(pa2)

rates=5
pa3=pa[::rates]
print(pa3)
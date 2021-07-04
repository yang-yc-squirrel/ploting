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
while(True):
    dii=di*i
    dis=[str(j) for j in dii]
    divs="".join(dis)
    div=eval(divs)


    if(divmod(n,div)[1]==0):
        res=i
        break
    i+=1
print(res)
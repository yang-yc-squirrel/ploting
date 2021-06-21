import matplotlib.pyplot
import numpy
import pandas
import random
import functools
import itertools

def inputstr():
    while(True):
        s = input("please input s:")
        if (s=="ab" or s=="ac"):
            break
        else:
            print("error")

    print("end")
    return s

s=inputstr()
print(s)
import matplotlib.pyplot
import numpy
import pandas

d=dict(a=[1,2,3],b=[5,6,7])
p=pandas.DataFrame(d,index=list(range(3)),columns=["b","a"])
print(p)
p=p.append([{"b":12,"a":108}],ignore_index=True)
print(p)


a=numpy.random.randint(2,15,size=(5,6))
print(a)
k=a.sum(axis=0)
print(k)

p1=pandas.DataFrame(a,columns=list("abcdef"))
print(p1)

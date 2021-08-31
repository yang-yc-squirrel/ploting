import numpy
import re
import time
import random
import itertools
import datetime
import matplotlib.pyplot
'''while(True):
    try:
        a = int(input("please input a number:"))
    except ValueError:
        print("error, reenter")
    else:
        break


n=1
while(True):
    seq=[9]*n
    s_seq=[str(i) for i in seq]
    vals=int("".join(s_seq))
    if(divmod(vals,a)[1]==0):
        res=n
        break
    else:
        n+=1
print("answer is {res}".format(res=res))'''



print(time.time())
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

d=datetime.date.today()
d=d.strftime("%Y year %m month %d day")
d1=datetime.time(12,23,22)
print(d1.second)
print(d)

d2=datetime.datetime.now()
print(d2)
d3=d2.strftime("%Y-%m-%d %H:%M:%S")
print(d3)
print(d2)

d5=datetime.datetime.fromtimestamp(time.time())
print(d5)

x=numpy.arange(0,10,0.1)
print(x)
y=numpy.cos(x)
print(y)

aa=[chr(ord("a")+i) for i in random.shuffle(list(range(10)))]
bb=[random.choice(list(range(10,30,2))) for i in range(7)]
print("aa is {0} \n bb is {1} \n".format(aa,bb))

dd=dict(itertools.zip_longest(aa,bb,fillvalue=200))
print(dd)

print(dd.keys())
print(dd.values())
print(dd.items())

print(dd.get("b","error"))
dd["x"]=12306
print(dd)
print("next".center(30,"-"))

def F(x,y):
    s2=0.01*abs(x+10)
    s1=100*((abs(y-0.01*(x**2)))**0.5)
    res=s1+s2
    return res

f=matplotlib.pyplot.figure()
f1=f.add_subplot(2,1,1)
matplotlib.pyplot.sca(f1)
matplotlib.pyplot.plot(x,y,color=(1,0,0))
matplotlib.pyplot.xticks(numpy.arange(0,11,1),[chr(ord("a")+i) for i in range(11)],fontproperties="Times New Roman",size=30)
matplotlib.pyplot.yticks(numpy.linspace(-1,1,5),fontproperties="Times New Roman",size=30)
f1.set_title("Cartesian",fontdict={"family":"Times New Roman","size":20})

f2=f.add_subplot(2,2,3,projection="polar")
matplotlib.pyplot.sca(f2)
th=[numpy.pi*i*0.1 for i in range(0,6,1)]
r=numpy.random.randint(2,7,size=(1,6)).flatten()
f2.scatter(th,r,color="red")
f2.set_rticks(numpy.arange(0,7,0.1))
f2.set_rlim([0,9])
f2.set_rlabel_position(320)
f2.set_title("polar",fontdict={"family":"Times New Roman","size":20})

f3=f.add_subplot(2,2,4,projection="3d")
matplotlib.pyplot.sca(f3)
p=numpy.linspace(-5,5,100)
x,y=numpy.meshgrid(p,p)
print(x)
print(y)
z=numpy.zeros(shape=(100,100))
for i in range(100):
    for j in range(100):
        z[i,j]=F(x[i,j],y[i,j])
f3.plot_surface(x,y,z,cmap=matplotlib.pyplot.get_cmap("hot"))
f3.view_init(30,50)
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
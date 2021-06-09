import numpy
import random
import matplotlib.pyplot
import mpl_toolkits.mplot3d

def initpso(nums,dims,ub,lb):
    X=numpy.zeros(shape=(nums,dims))
    for i in range(nums):
        for j in range(dims):
            X[i,j]=random.random()*(ub[j]-lb[j])+lb[j]
    return X

def overborder(X,ub,lb):
    nums=X.shape[0]
    dims=X.shape[1]
    for i in range(nums):
        for j in range(dims):
            if(X[i,j]>ub[j]):
                X[i,j]=ub[j]
            if(X[i,j]<lb[j]):
                X[i,j]=lb[j]
    return X

def pso(nums,dims,ub,lb,T,func):
    X=initpso(nums,dims,ub,lb)
    V=numpy.zeros(shape=(nums,dims))

def testfunc(x):
    n=len(x)
    s1=0
    s2=1
    for i in range(n):
        s1=s1+(x[i]**2)
    s1=s1/4000
    for j in range(1,n+1,1):
        s2=s2*numpy.cos(x[j-1]/(j**0.5))
    res=s1-s2+1
    return res

f=matplotlib.pyplot.figure()
p=mpl_toolkits.mplot3d.Axes3D(f)

xdata=numpy.linspace(-60,60,500)
ydata=numpy.linspace(-60,60,500)
x,y=numpy.meshgrid(xdata,ydata)

z=numpy.zeros(shape=(500,500))
for i in range(500):
    for j in range(500):
        vec=numpy.array([x[i,j],y[i,j]])
        z[i,j]=testfunc(vec)

p.plot_surface(x,y,z,cmap=matplotlib.pyplot.get_cmap("winter"))
matplotlib.pyplot.show()

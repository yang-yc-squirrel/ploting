import numpy
import matplotlib.pyplot
import mpl_toolkits.mplot3d

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
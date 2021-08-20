import numpy
import matplotlib.pyplot
while(True):
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
print("answer is {res}".format(res=res))


x=numpy.arange(0,10,0.1)
print(x)
y=numpy.cos(x)
print(y)

f=matplotlib.pyplot.figure()
f1=f.add_subplot(2,1,1)
matplotlib.pyplot.sca(f1)
matplotlib.pyplot.plot(x,y,color=(1,0,0))
matplotlib.pyplot.xticks(numpy.arange(0,11,1),fontproperties="Times New Roman",size=30)
matplotlib.pyplot.yticks(numpy.linspace(-1,1,5),fontproperties="Times New Roman",size=30)

f2=f.add_subplot(2,1,2,projection="polar")
matplotlib.pyplot.sca(f2)
th=[numpy.pi*i*0.1 for i in range(0,6,1)]
r=numpy.random.randint(2,7,size=(1,6)).flatten()
f2.scatter(th,r,color="red")
f2.set_rticks(numpy.arange(0,7,0.1))


matplotlib.pyplot.show()
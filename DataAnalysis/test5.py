import numpy
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


x=numpy.arange(0,10,0.1)
print(x)
y=numpy.cos(x)
print(y)


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
p=numpy.linspace(0,10,100)
x,y=numpy.meshgrid(p,p)
print(x)
print(y)

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
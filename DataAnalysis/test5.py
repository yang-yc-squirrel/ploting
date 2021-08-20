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

f=matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x,y,color=(1,0,0))
matplotlib.pyplot.xticks(numpy.arange(0,11,1),fontproperties="Times New Roman",size=30)
matplotlib.pyplot.yticks(numpy.linspace(-1,1,5),fontproperties="Times New Roman",size=30)
matplotlib.pyplot.show()
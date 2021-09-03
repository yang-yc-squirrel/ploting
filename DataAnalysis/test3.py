import matplotlib.pyplot
import random
def Hammingcode(m):
    k=1
    while(True):
        ri=pow(2,k)
        le=m+1+k
        if(ri>=le):
            res=k
            break
        k+=1
    return res

a=Hammingcode(16)
print(a)

f=matplotlib.pyplot.figure()
f1=f.add_subplot(2,1,1)
f2=f.add_subplot(2,2,3)
f3=f.add_subplot(2,2,4)

matplotlib.pyplot.sca(f1)
ax1=matplotlib.pyplot.gca()

x=list(range(2,12,2))
a=[random.randint(2,10) for i in range(5)]
b=[random.randint(5,10) for i in range(5)]
matplotlib.pyplot.bar(x,a,width=0.4,facecolor="#ff0000")
matplotlib.pyplot.bar(x,b,bottom=a,width=0.4,facecolor="#0000ff")

x_tick1=ax1.get_xticklabels()
[n.set_fontname("Times New Roman") for n in x_tick1]
y_tick1=ax1.get_yticklabels()
[n.set_fontname('Times New Roman') for n in y_tick1]

for i in range(5):
    matplotlib.pyplot.text(x[i]-0.25,a[i]+b[i]+0.5,str(format(a[i]+b[i],"0.2f")),fontdict={"family":"Times New Roman","size":15})

matplotlib.pyplot.title("Histogram", fontdict={"family":"Times New Roman","size": 14})

matplotlib.pyplot.show()
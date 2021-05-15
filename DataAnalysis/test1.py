def fib(n):
    a=1
    b=1
    while(True):
        yield a
        a,b=b,a+b
        if(n==1):
            break
        n-=1

g=fib(10)
s=0
while(True):
    try:
        j=next(g)
        print(j)
        s+=j
    except StopIteration:
        break
print("end".center(50,"-"))
print("{na}".format(na=s))


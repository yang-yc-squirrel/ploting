def PascalTriangleRow(n):
    if(n==0):
        res=[1]
    else:
        if(n==1):
            res=[1,1]
        else:
            storages=[PascalTriangleRow(n-1)[i:i+2] for i in range(0,len(PascalTriangleRow(n-1))-1,1)]
            res=[sum(k) for k in storages]
            res.append(1)
            res.insert(0,1)
    return res




while(True):
    try:
        n=int(input("please enter the number of rows:"))
    except ValueError:
        print("error! please enter again")
    else:
        print("Received n")
        break

nlist=list(range(n))
print("begin print".center(20,"-"))
for i in nlist:
    print(PascalTriangleRow(i))



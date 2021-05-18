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
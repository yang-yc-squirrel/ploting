def repolish(s):
    numlist=list(range(0,10,1))
    symlist=[chr(ord("a")+i) for i in range(26)]+[chr(ord("A")+j) for j in range(26)]
    opelist=["+","-","*","/","(",")"]
    stack1=[]
    stack2=[]
    li=list(s)
    for k in li:
        if(k in numlist or k in symlist):
            stack2.append(k)
        else:
            if(k in opelist):
                if(len(stack1)==0):
                    stack1.append(k)
                else:
                    finalope=stack1[len(stack1)-1]
                    



    return li

s=input("please input an expression:")
li=repolish(s)
print(li)
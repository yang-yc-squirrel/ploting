def repolish(s):
    numlist=[str(i) for i in range(0,10,1)]
    symlist=[chr(ord("a")+i) for i in range(26)]+[chr(ord("A")+j) for j in range(26)]
    opelist=["+","-","*","/","(",")"]
    prioritylist=[0,0,1,1,2,2]
    opedict=dict(zip(opelist,prioritylist))
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
                    if(k=="("):
                        stack1.append(k)
                    else:
                        if(k==")"):
                            while(True):
                                finalope = stack1[len(stack1) - 1]
                                if(finalope=="("):
                                    break
                                stack2.append(finalope)
                                stack1.pop()
                        else:
                            finalope = stack1[len(stack1) - 1]
                            if(opedict.get(k)>opedict.get(finalope)):
                                stack1.append(k)
                            else:
                                while(True):
                                    finalope = stack1[len(stack1) - 1]
                                    stack2.append(finalope)
                                    stack1.pop()
                                    finalope = stack1[len(stack1) - 1] if len(stack1)>=1 else "^"
                                    if(opedict.get(k)>opedict.get(finalope,-1)):
                                        stack1.append(k)
                                        break

    stack1.reverse()
    stack2.extend(stack1)
    res=[]
    while(len(stack2)!=0):
        res.append(stack2.pop())
    res="".join(res)
    return res

s=input("please input an expression:")
res=repolish(s)
print(res)
import operator
def conflict(pos):
    for i in range(0,len([pos])-1,1):
        for j in range(i+1,len(pos),1):
            if(operator.eq(pos[i],pos[j]) or operator.eq(abs(i-j),abs(pos[i]-pos[j]))):
                res=True
                break
    else:
        res=False
    return res

def initpos(n):
    pos=[0 for i in range(n)]
    return pos

solnums=0
n=8
pos=initpos(n)
k=1
while(True):
    while(True):
        if (conflict(pos[0:k + 1:1])):
            pos[k] += 1
            if (operator.ge(pos[k], n)):
                pos[k] = 0
                k -= 1
                pos[k] += 1
        else:
            break
    
    k=k+1
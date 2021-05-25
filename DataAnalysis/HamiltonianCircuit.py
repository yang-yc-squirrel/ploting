import numpy
import random

def fingdcircle(adjmat):
    n=adjmat.shape[0]
    x=numpy.array([0 for i in range(n)])
    visited=numpy.array([0 for i in range(n)])
    k=0
    x[k]=0
    visited[x[k]]=1
    while(k<n):
        while(True):
            x[k] = x[k] + 1
            if (x[k] >= n):
                visited[x[k - 1]] = 0
                x[k] = 0
                k -= 1
                continue
            if (visited[x[k]]==0 and adjmat[x[k],x[k-1]]==1):
                visited[x[k]]=1
                break
        k+=1
    return visited


n=6
adjmat=numpy.zeros(shape=(n,n))
xl=list(range(n))
yl=list(range(n))
connect_p=[(random.choice(xl),random.choice(yl)) for k in range(8)]
for points in connect_p:
    i=points[0]
    j=points[1]
    adjmat[i,j]=1
    adjmat[j,i]=1

visited=fingdcircle(adjmat)
print(visited)
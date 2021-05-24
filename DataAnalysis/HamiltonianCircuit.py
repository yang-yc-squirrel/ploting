import numpy
def fingdcircle(adjmat):
    n=adjmat.shape[0]
    x=numpy.zeros(shape=(1,n)).flatten()
    visited=numpy.zeros(shape=(1,n)).flatten()
    k=0
    x[k]=0
    visited[x[k]]=1
    while(k<n):
        while(True):
            x[k] = x[k] + 1
            if (visited[x[k]]==0 and adjmat[x[k],x[k-1]]==1):
                visited[x[k]]=1
                break
            if(x[k]>=n):
                visited[x[k]]=0
                visited[x[k-1]]=0
                x[k]=0
                k-=1
                



g=numpy.zeros(shape=(1,10)).flatten()
print(g)
print(g[5])
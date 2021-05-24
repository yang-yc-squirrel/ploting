import numpy
def fingdcircle(adjmat):
    n=adjmat.shape[0]
    x=numpy.zeros(shape=(1,n)).flatten()
    visited=numpy.zeros(shape=(1,n)).flatten()
    k=0
    x[k]=0
    visited[x[k]]=1
    for k in range(1,n,1):
        x[k]=x[k]+1
        if()


g=numpy.zeros(shape=(1,10)).flatten()
print(g)
print(g[5])
import itertools
def subseq(s):
    ls=len(s)
    eledel=[]
    subnums=0
    indexlist=list(range(ls))
    for i in range(1,ls,1):
        subdel=list(itertools.combinations(indexlist,i))
        subnums+=len(subdel)
        eledel.extend(subdel)

    x=list(range(subnums))
    y=[]
    for i in eledel:
        retainindex=[j for j in range(ls) if j not in i]
        retains=[s[k] for k in retainindex]
        s_n="".join(retains)
        y.append(s_n)

    d=dict(zip(x,y))
    res=y.copy()

    return subnums,res

subnums,res=subseq("abcde")
print("The number of subsequences is: {0}".format(subnums))
print("List subsequences: {ls}".format(ls=res))



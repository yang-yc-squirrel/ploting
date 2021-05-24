import numpy
def knapsack_init(val_li,wei_li,nums,volume):
    ans = numpy.zeros(shape=(nums+1, volume+1))
    for i in range(0,nums+1,1):
        for j in range(0,volume+1,1):
            ans[i,j]=-1
    return ans
def knapsack_plan(val_li,wei_li,i,j,ans):
    if(ans[i,j]!=-1):
        return ans[i,j]



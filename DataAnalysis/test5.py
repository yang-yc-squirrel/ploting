while(True):
    try:
        a = int(input("please input a number:"))
    except ValueError:
        print("error, reenter")
    else:
        break


n=1
while(True):
    seq=[9]*n
    s_seq=[str(i) for i in seq]
    vals=int("".join(s_seq))
    if(divmod(vals,a)[1]==0):
        res=n
        break
    else:
        n+=1
print("answer is {res}".format(res=res))

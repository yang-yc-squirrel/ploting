a=[chr(ord("a")+i) for i in range(19)]
print(a)
a.pop(0)
print(a)
a.pop(2)
print(a)
d=dict([("a",5),("b",36),("c",25)])
print(d)
print(d.get("a"))


print(divmod(459,27))


g=list(range(20))
print(g)
print(g[0:7])
k=slice(0,7)
print(g[k])

for i in range(0,100,7):
    print(i)



print(a)
p="".join(a)
print(type(p))
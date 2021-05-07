#second max no
n=[24,435,54,142,6567,64363,13]
i=0
b=n[i]
while i<len(n):
    if b<n[i]:
        c=n[i]
    i+=1
n.remove(c)
k=0
s=n[k]
while k<len(n):
    if s<n[k]:
        c=n[k]
    k+=1
print(c)
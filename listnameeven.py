l=["ankita","pisal","smita","akhilesh","shantaram"]
i=0
while i<len(l):
    if len(l[i])%2==0:
        print(l[i],len(l[i]),"is even")
    else:
        print(l[i],len(l[i]),"is odd")
    i=i+1
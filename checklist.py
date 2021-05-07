a=["a","a","s","s","d","d"]
b=[]
b.append(a)
s=[]
i=0
while i<len(a):
        if a[i]  not in b:
            s.append(a[i])
        i+=1
print(s)
#max no here we put a[i]<m then we will get min number
a=[13,32,5,78,786,342,65,987]
i=0
max=a[i]
min=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
    i+=1
print("max number",max)
print("minimum",min)

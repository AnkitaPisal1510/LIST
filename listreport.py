'''marks=[
   [78,76,94,86,88],
   [91,71,98,65,76],
   [95,45,78,52,49] 
]
i=0
s=0
m=len(marks[0])and len(marks[1])and len(marks[2])
while i<m:
    m1=marks[0][i]+marks[1][i]+marks[2][i]
    s=s+m1          
    i+=1
print(s)'''
a=[
    [78,76],
    [91,71],
    [95]
    ]
i=0
sum=0
ave=0
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[i][j]
        c=len(a[i])
        j+=1
    sum+=s
    i+=1
    print("average=",s/c)
print("total list average=",sum/len(a))
print("list =",a,"sum =",sum)

m=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
A=15
k=0
while k<len(m):
    column=0
    sum=0
    l=len(m[k])
    while column<l:
        sum=sum+m[k][column]
        column+=1
    print(sum,"column")
    x=sum+sum+sum
    k+=1
print(x)
i=0
while i<len(m):
    row=0
    sum1=0
    while row<len(m[i]):
        sum1+=m[row][row]
        row+=1
    print(sum1,"row")
    h=sum1+sum1+sum1
    i+=1
print(h)
s=m[0][0]+m[1][1]+m[2][2]
d=m[0][2]+m[1][1]+m[2][0]
if s==A:
    if d==A:
        mn=s+d
        print("diagonal:",mn)
        if sum==sum1==A:
                print("it is majic square")
        else:
            print("it is not majic square")
    else:
        print("oit is not majic square")
else:
    print("it is not majic square")
    
#even odd in list
s=[]
e=[]
o=[]
p=[]
n=[]
sum=sum1=sum2=sum3=sum4=0
ave=ave1=0
size=int(input("enter the size of the list"))
i=0
c=0
while i<size:
    user=int(input("enter the numbers"))
    s.append(user)
    sum=sum+user 
    if user%2==0:
        sum1=sum1+user
        ave=sum1/len(s)
        e.append(user)
    if user%2!=0:
        sum2=sum2+user
        ave1=sum2/len(s)
        o.append(user)
    if user>0:
        sum3+=user
        n.append(user)
    if user<0:
        sum4+=user
        p.append(user)
    i=i+1
print("list=",s,"sum of list=",sum,"average=",ave)
print("even number list=",e,"even numbers sum=",sum1,"average of even numbers",ave1)
print("odd number list=",o,"odd number sum=",sum2,"average of odd numbers",ave)
print("positive integer list=",p,"positive  numbers sum",sum3)
print("negative integer list",n,"negative numbers sum",sum4)

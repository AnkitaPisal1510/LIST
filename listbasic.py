#10 user input lo use 1 list me put karo fir check karo vo number list me hai ya nahi
i=0
d=[]
while i<10:
    n=int(input("enter the number"))
    i+=1
    d.append(n)
n1=int(input("enter"))
if n1 in d:
    print("present in list")
else:
    print("present nahi hai")

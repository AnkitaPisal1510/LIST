 marks=[50,40,23,70,56,12,5,10,7]
length=len(marks)
i=0
less40=0
more20=0
mar1=[]
mar2=[]
while i<length:
    mark=marks[i]
    if mark<40:
        less40+=1
        mar1.append(mark)
    else:
        more20+=1
        mar2.append(mark)
    i+=1
print("less40",mar1,"=",less40)
print("more20",mar2,"=",more20)

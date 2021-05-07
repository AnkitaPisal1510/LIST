'''paisa=[100000,9000000,10000000,3214,123456,567890,2134,4635,76,200000000,12345678910,65765,547,523546,653]
c1=0
c2=0
c3=0
i=0
while i<len(paisa):
    if paisa[i]<=12345678910 and paisa[i]>=10000000:
        c3+=1
    elif paisa[i]>=100000 and paisa[i]<=9000000:
        c2+=1
    else:
        c1+=1
    i+=1
print(c3,"corepati")
print(c2,"lakhpati")
print(c1,"dilvale")'''


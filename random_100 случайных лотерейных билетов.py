from random import*
a=[0,1,2,3,4,5,6,7,8,9]
a1=[]
while len(a1)<100:
    b=sample(a,7)
    if b[0]!=0 and b not in a1:
        a1.append(b)
        b1=''
        for i in b:
            b1+=str(i)
        print(b1)




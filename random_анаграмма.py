from random import*
a=input()
a1={i:a.count(i) for i in a}
b=[i for i in a]
b1={}
while a1!=b1 and list(a)==b:
    shuffle(b)
    b1 = {i: b.count(i) for i in b}
b2=''
for i in b:
    b2+=i
print(b2)






from random import*
# a=[]
# for i in range(int(input())):
#    a.append(input())
a=[input() for i in range(int(input()))]
i=0
b=[]
while i<len(a):
    a1=choice(a)
    if a1!=a[i] and a1 not in b:
        b.append(a1)
        print(a[i] + '-' + b[i])
        i+=1






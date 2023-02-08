# a=[100, 55, 77, 55, 89]
a=[1,2,3]
# a=list(map(int,input().split()))
s={}
counter=-3
for i in range(len(a)-2):
    if len(s)==0:
        s={a[-2]:a[-1]}
    s={a[counter]:s}
    counter-=1
print(s)
# еще решение через рекурсию




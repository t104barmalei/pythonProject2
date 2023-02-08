a={}
for i in range(int(input())):
    a1=input().split()
    a[a1[0]]=a1[1]
# print(a)
m=input()
for i in a:
    if i ==m:
        print(a[i])
    if a[i]==m:
        print(i)


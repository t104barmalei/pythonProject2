n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
# print(a)
a1=[]
for i in range(n):
    a2=[]
    for j in range(n):
        a2.append(a[j][i])
    print(*a2)
    a1.append(a2)




n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
# print(a)
a1=[]
for i in range(n):
    # a2=[]
    for j in range(n):
        if i>=n-1-j:
            a1.append(a[i][j])

print(max(a1))



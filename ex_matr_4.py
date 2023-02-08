n=int(input())
a=[['.']*n for i in range(n)]
# print(a)
print(int(n/2),n/2)
for i in range(n):
    for j in range(n):
        if i==j or i==n-j-1 or i==int(n/2) or j==int(n/2):
            a[i][j]='*'
    print(*a[i])





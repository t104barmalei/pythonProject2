n=int(input())
for i in range(n):
    a=[]
    for j in range(n):
        if j==n-i-1:
            a.append(1)
        if i+j+1>n:
            a.append(2)
        if i+j+1<n:
            a.append(0)
    print(*a)
# еще решение
# n = int(input())
# [print(*[(i > (n - j - 1)) + int(i >= (n - j - 1)) for j in range(n)]) for i in range(n)]




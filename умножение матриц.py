n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
input()
n1,m1=map(int,input().split())
b=[list(map(int,input().split())) for i in range(n1)]
c=[[0]*n for i in range(m1)]
for i in range(n):
    for j in range(m1):
        for k in range(m):
            c[i][j]+=a[i][k]*b[k][j]
for i in c:
    print(*i)



#




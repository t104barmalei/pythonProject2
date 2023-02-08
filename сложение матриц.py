n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
input()
b=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    c=[]
    for j in range(m):
        c.append(a[i][j]+b[i][j])
    print(*c)

#еще решение
# n,m = map(int,input().split())
# a=[[*map(int,input().split())]for _ in '.'*n]
# input()
# b=[[*map(int,input().split())]for _ in '.'*n]
# [print(*(i+j for i,j in zip(l,k))) for l,k in zip(a,b)]





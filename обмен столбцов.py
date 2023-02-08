# Программа должна вывести указанную таблицу с замененными столбцами.
n=int(input())
m=int(input())
a=[]
a1=[]
for i in range(n):
    a.append(list(map(int,input().split())))
# print(a)
b,c=map(int,input().split())
for i in range(n):
    for j in range(m):
        if j==c:
            a[i][c],a[i][b]=a[i][b],a[i][c]
    print(*a[i])
# еще решение
# n, m = int(input()), int(input())
# mult = [input().split() for _ in range(n)]
# i, j = map(int, input().split())
# for c in mult:
#   c[i], c[j] = c[j], c[i]
#   print(*c)




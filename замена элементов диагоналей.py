# Программа должна вывести указанную таблицу с замененными столбцами.
n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
a=[list(map(int,input().split())) for i in range(n)]
# print(a)
for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j], a[n - i - 1][i] = a[n - i - 1][i], a[i][j]

# for i in range(n):
#     print(*a[i])

[print(*a[i]) for i in range(n)]
# еще решение





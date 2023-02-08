# Проверка мтарицы на Латинский квадрат
# Латинским квадратом порядка nn называется квадратная матрица
# размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до n.
n=int(input())
a=[input().split() for i in range(n)]
a1=[]
for i in range(n):
    a1.append(i+1)
b=True
a3=[]
for i in range(n):
    a2=[]
    for j in range(n):
        if a[i].count(a[i][j])!=1:
            b=False
        elif int(a[i][j]) not in a1:
            b=False
        elif int(a[j][i]) not in a1:
            b = False
        a2.append(a[j][i])
    a3.append(a2)
for i in range(n):
    for j in range(n):
        if a3[i].count(a3[i][j])!=1:
            b=False
            break
if b:
    print('YES')
else:
    print('NO')








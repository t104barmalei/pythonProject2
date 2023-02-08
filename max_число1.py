# Напишите программу,  которая выводит след заданной квадратной матрицы..
n = int(input())
a = []
a1 = []
for i in range(n):
    a.append(list(map(int, input().split())))
# print(a)
for i in range(n):
    for j in range(n):
        if i >= j and i<=n-1-j:
            a1.append(a[i][j])
        if i <=j and i>=n-1-j:
            a1.append(a[i][j])
print(a1)
print(max(a1))
# еще решение
# n = int(input())
# a = [[*map(int, input().split())] for _ in range(n)]
# print(max(a[i][j] for i in range(n) for j in range(n) if j <= i <= n - j - 1 or j >= i >= n - j - 1))

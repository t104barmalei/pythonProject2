# Напишите программу,  которая выводит след заданной квадратной матрицы..
n = int(input())
a = []
a1 = []
for i in range(n):
    a.append(list(map(int, input().split())))
# print(a)
for i in range(n):
    for j in range(n):
        if i >= j:
            a1.append(a[i][j])
print(max(a1))
# еще решение
# for i in range(int(input())):
#     str=list(map(int,input().split()))
#     sr=sum(str)/len(str)
#     print(sum(j>sr for j in str))

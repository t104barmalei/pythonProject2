# Напишите программу,  которая выводит след заданной квадратной матрицы..
# n=int(input())
# a=[]
# sum=0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             sum+=a[i][j]
# print(sum)
# еще решение
sum=0
for i in range(int(input())):
    sum+=int(input().split()[i])
print(sum)









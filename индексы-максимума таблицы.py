# Программа должна вывести два числа: номер строки и номер столбца,
# в которых стоит наибольший элемент таблицы. Если таких элементов несколько,
# то выводится тот, у которого меньше номер строки, а если номера строк равны
# то тот, у которого меньше номер столбца.
# n=int(input())
# m=int(input())
# a=[]
# a1=[]
# sum=0
# for i in range(n):
#     a.append(list(map(int,input().split())))
# for i in range(n):
#     a1.append(max(a[i]))
# mmax=max(a1)
# str=n
# stlb=m
# for i in range(n):
#     for j in range(m):
#         if a[i][j]==mmax:
#             if i<str:
#                 str=i
#                 stlb=j
#             elif str==i:
#                 if j<stlb:
#                     stlb=j
# print(str,stlb)
# еще решение
n, m = int(input()), int(input())
matrix = [int(num) for _ in range(n) for num in input().split()]
print(matrix.index(max(matrix)) // m, matrix.index(max(matrix)) % m)




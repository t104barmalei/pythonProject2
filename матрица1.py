# Напишите программу, которая сначала считывает элементы матрицы
# один за другим, затем выводит их в виде матрицы.
n=int(input())
m=int(input())
for i in range(n):
    a=[]
    for j in range(m):
        a.append(input())
    print(*a)
# или через строки
# n=int(input())
# m=int(input())
# for i in range(n):
#     a=''
#     for j in range(m):
#         a+=' '+input()
#     print(a)








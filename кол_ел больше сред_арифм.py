# Напишите программу,  которая выводит след заданной квадратной матрицы..
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    count=0
    for j in range(n):
        if a[i][j]>sum(a[i])/n:
            count+=1
    print(count)
# еще решение
# for i in range(int(input())):
#     str=list(map(int,input().split()))
#     sr=sum(str)/len(str)
#     print(sum(j>sr for j in str))










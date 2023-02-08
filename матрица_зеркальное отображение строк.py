# Программа должна вывести зеркальное отображение строк.
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
# print(a)
for i in range(int(n/2)):
    a[i], a[n-i-1]= a[n-i-1], a[i]
# for i in range(n):
#     print(*a[i])
[print(*a[i]) for i in range(n)]
# еще решение
# matrix = [input().split() for _ in range(int(input()))]
# [print(*r) for r in matrix[::-1]]
# вар2
# n = int(input())
# res = [[int(x) for x in input().split()] for _ in range(n)]
# for j in range(n - 1, -1, -1):
#     print(*res[j])





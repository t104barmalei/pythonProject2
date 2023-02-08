# поворот матрицы на 90 градусов по часовой
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
# print(a)
a1=[]
for i in range(n):
    a2=[]
    for j in range(n-1,-1,-1):
        a2.append(a[j][i])
    a1.append(a2)

# for i in range(n):
#     print(*a[i])
[print(*a1[i]) for i in range(n)]



# еще решение
# matrix = [input().split() for _ in range(int(input()))]
# [print(*r) for r in matrix[::-1]]
# вар2
# n = int(input())
# res = [[int(x) for x in input().split()] for _ in range(n)]
# for j in range(n - 1, -1, -1):
#     print(*res[j])





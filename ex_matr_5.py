# Проверка мтарицы на симметеричность относительно побочной диагонали
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    a[i].reverse()
print(a)
a1=[]
for i in range(n):
    for j in range(n):
        if a[i][j]!=a[j][i]:
            a1.append(False)
            break
        else:
            a1.append(True)
if False in a1:
    print("NO")
else:
    print("YES")
# еще решение
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# a1=[]
# for i in range(n):
#     for j in range(n):
#         if a[i][j]!=a[n - j - 1][n - i - 1]:
#             a1.append(False)
#             break
#         else:
#             a1.append(True)
# if False in a1:
#     print("NO")
# else:
#     print("YES")






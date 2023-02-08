a={}
for i in range(int(input())):
    a1=input().lower().split()
    a.setdefault(a1[1],[]).append(a1[0])
    # if a1[1] not in a:
    #     a[a1[1]]=[a1[0]]
    # else:
    #     a[a1[1]].append(a1[0])
# print(a)
for i in range(int(input())):
    print(*a.setdefault(input().lower(),['абонент не найден']))
# # еще решение
#
# Sample Input:
# 3
# 79184219577 Женя
# 79194249271 Руслан
# 79281234567 Женя
# 3
# Руслан
# женя
# Рустам
# Sample Output:
# 79194249271
# 79184219577 79281234567
# абонент не найден
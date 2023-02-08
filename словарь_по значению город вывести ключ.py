a={}
for i in range(int(input())):
    a1=input().split()
    a[a1[0]]=a1[1:]
print(a)
for i in range(int(input())):
    m=input()
    for key,value in a.items():
        if m in value:
            print(key)

# # еще решение
# d = {}
# for _ in range(int(input())):
#     a, *b = input().split()
#     d.update(dict.fromkeys(b, a))
# [print(d[input()]) for _ in range(int(input()))]

#  программa, которая для каждого города выводит, в какой стране он находится.
# 2
# Германия Берлин Мюнхен Гамбург Дортмунд
# Нидерланды Амстердам Гаага Роттердам Алкмар
# 4
# Амстердам
# Алкмар
# Гамбург
# Гаага

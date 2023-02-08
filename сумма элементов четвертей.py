# Напишите программу,  вычисляет сумму элементов: верхней четверти;
# правой четверти; нижней четверти; левой четверти.
n = int(input())
a = []
a1 = []
a2 = []
a3 = []
a4 = []
for i in range(n):
    a.append(list(map(int, input().split())))
# print(a)
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            a1.append(a[i][j])
        if i < j and i > n - 1 - j:
            a2.append(a[i][j])
        if i > j and i > n - 1 - j:
            a3.append(a[i][j])
        if i > j and i < n - 1 - j:
            a4.append(a[i][j])
print(f"Верхняя четверть: {sum(a1)}")
print(f"Правая четверть: {sum(a2)}")
print(f"Нижняя четверть: {sum(a3)}")
print(f"Левая четверть: {sum(a4)}")


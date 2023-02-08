# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
# for i in range(int(input())):
#     s, virus, x  = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break

# еще одно решение
# a1 = [input() for i in range(int(input()))]
# for i in range(len(a1)):
#     if 'a' and 'n' in a1[i]:
#         a2 = a1[i][a1[i].find('a'):a1[i].rfind('n')]
#         if 'n' and 'o' in a2:
#             a3 = a2[a2.find('n'):a2.rfind('o')]
#             if 't' in a3:
#                 print(i + 1, end=' ')

# вар 3 без списка
for i in range(int(input())):
    a=input()
    if 'a' and 'n' in a:
        a2=a[a.find('a'):a.rfind('n')]
        if 'n' and 'o' in a2:
            a3=a2[a2.find('n'):a2.rfind('o')]
            if 't' in a3:
                print(i+1,end=' ')

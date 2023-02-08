b=input().split()
for i in range(len(b)):
    b[i]=b[i].lower().strip('.,!?:;-')
a={i:b.count(i) for i in b}
a1=[]
for i in a:
    if a.get(i)==min(a.values()):
        a1.append(i)
print(min(a1))
# # еще решение
# d = {}
# for w in input().split():
#     w = w.strip('.,!?:;-').lower()
#     d[w] = d.get(w, 0) + 1
# print(min(d.items(), key=lambda x: (x[1], x[0]))[0])
#
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
# без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.


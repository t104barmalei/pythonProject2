# Напишите программу для определения,
# является ли число произведением двух чисел из данного набора,
# выводящую результат в виде ответа «ДА» или «НЕТ» Само на себя
# число из набора умножиться не может, другими словами,
# два множителя должны иметь разные индексы в наборе
a=int(input())
a1=[]
for i in range(a):
    i=int(input())
    a1.append(i)
b=int(input())
a2=[]
for i in range(len(a1)):
    for j in range(len(a1)):
        if i!=j:
            a2.append(a1[i]*a1[j])
if b in a2:
    print('ДА')
else:
    print('НЕТ')




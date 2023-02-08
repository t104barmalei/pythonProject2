# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество
# подряд выпавших Решек.
# a=input()
# if a[0] != 'Р':
#     count = 0
# if a[0] == 'Р':
#     count = 1
# a1=[]
# for i in range(1,len(a)):
#     if a[i]==a[i-1] and a[i]=='Р':
#         count+=1
#     else:
#         a1.append(count)
#         count=1
# if 'Р' not in a:
#     print(0)
# elif a1 and 'Р' in a:
#     print(max(max(a1),count))
# elif not a1 and 'Р' in a:
#     print(count)
# самое простое решение!!!
s = input().split('О')
print(len(max(s)))







#На вход программе подается строка текста, содержащая символы. Напишите программу,
# которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# a= input().split()
# a1=[]
# count=1
# for i in range(1,len(a)):
#     if a[i] ==a[i-1]:
#         count+=1
#     else:
#         a1.append(list(a[i-1]*count))
#         count=1
# a1.append(list(a[i]*count))
# print(a1)


# еще решение
res = []
for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)














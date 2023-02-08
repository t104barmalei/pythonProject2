#На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
# Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

# a= input().split()
# a1=[]
# count=len(a)
# a1.append([])
# for i in range(len(a)):
#     a1.append([a[i]])
# for j in range(len(a),0,-1):
#     for i in range(len(a)):
#         if a[i:i+len(a)-j+2] not in a1:
#             a1.append(a[i:i+len(a)-j+2])
# print(a1)
#еще решение
raw = input().split()
new = [[]]
for i in range(len(raw)):
    for j in range(len(raw) - i):
        new.append(raw[j:j + i + 1])
print(new)









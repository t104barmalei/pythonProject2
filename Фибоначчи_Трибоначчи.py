# # последовательность Фибоначчи
# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2

# последовательность  Трибоначчи через списки
n = int(input())
f1, f2, f3 = 1, 1, 1
a=[]
for i in range(n):
    a.append(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3
print(*a)
# # еще решение через строки
# n = int(input())
# f1, f2, f3 = 1, 1, 1
# a=''
# for i in range(n):
#     a+=' '+str(f1)
#     # print(f1)
#     f1, f2, f3 = f2, f3, f1 + f2 + f3
# print(a)
# последовательность Трибоначчи
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3


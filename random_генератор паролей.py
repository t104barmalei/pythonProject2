import string
from random import*
n, m = int(input()), int(input())
a=string.ascii_letters+string.digits
a1=''
for i in a:
    if i not in ('l','I','1','o','O','0'):
        a1+=i
# print(a1)
c=[]
for i in range(n):
    b=''
    for j in range(m):
        b+=choice(a1)
    if b not in c:
        c.append(b)
    print(b)

# # еще решение через функции
# def generate_password(length):
#     b1=''
#     while len(b1)<length:
#         b1+=choice(a1)
#     return b1
#
# def generate_passwords(count, length):
#     c=[]
#     for i in range(count):
#         d=generate_password(length)
#         if d not in c:
#             c.append(d)
#     # print(c)
#     return c
#
#
# import string
# from random import*
# a=string.ascii_letters+string.digits
# a1=''
# for i in a:
#     if i not in ('l','I','1','o','O','0'):
#         a1+=i
#
# n, m = int(input()), int(input())
#
# # print(generate_password(m))
# for i in generate_passwords(n,m):
#     print(i)







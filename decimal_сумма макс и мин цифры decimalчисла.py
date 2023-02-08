# from decimal import*
#
# s=input()
# a=[]
# for i in s:
#     if i.isdigit():
#         a.append(Decimal(i))
# print(max(a)+min(a))

# еще решение
from decimal import *
num = Decimal(input())
a=[]
for i in str(num):
    if i.isdigit():
        a.append(Decimal(i))
print(max(a)+min(a))

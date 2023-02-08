import string
from random import*
a=string.digits
b=''
for i in range(5):
    c=''
    for j in range(5):
        if i==j==2:
            c+='0'.ljust(3)
        else:
            d=str(randint(1, 75))
            while d in b+c:
                d=str(randint(1, 75))
            c += d.ljust(3)
    b+=c
    print(c)
# # еще решение более рациональное
# from random import *
# numbers = set(sample([i for i in range(1, 76)], 25))
# s = [[numbers.pop() for _ in range(5)] for _ in range(5)]
# s[2][2] = 0
# for row in s:
#     print(*(str(k).ljust(3) for k in row))






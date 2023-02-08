from fractions import Fraction
from math import*
n=int(input())
a=0
for i in range(1,n+1):
    a+=1/Fraction(factorial(i))
print(a)

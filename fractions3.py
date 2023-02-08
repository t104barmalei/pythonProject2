from fractions import Fraction
from math import*
n=int(input())
a=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n and gcd(i,j)==1 and i<j:
            a.append(Fraction(i,j))

# print(a)
print(max(a))
# Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n
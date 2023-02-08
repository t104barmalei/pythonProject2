from fractions import Fraction
from math import*
n=int(input())
a=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i/j<1 and gcd(i,j)==1 and j<=n:
            a.append(Fraction(i,j))
for i in (sorted(a)):
    print(i)

# Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1,
# знаменатель которых не превосходит nn
import random

n = 10**6       # количество испытаний
count=0
for i in range(n):
    x=random.uniform(-2,2)
    y=random.uniform(-2,2)
    if x**3+y**4+2>=0 and x*3+y**2<=2:
        count+=1
print((count/n)*16)


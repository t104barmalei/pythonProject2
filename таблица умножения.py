# таблица умножения.
n=int(input())
m=int(input())
a1=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append(str(i*j).ljust(3))
    print(*a)



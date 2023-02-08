n=int(input())
a=set(input())
for i in range(n-1):
    a.intersection_update(set(input()))
print(*sorted(a))
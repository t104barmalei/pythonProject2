a=input().split()
result = {}
b=[]
for num in a:
    result[num] = result.get(num, 0) + 1
    b.append(result[num])
print(*b)
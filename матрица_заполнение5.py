n,m=map(int,input().split())
a=[str(i) for i in range(1,m+1)]
for i in range(1,n+1):
    print(*a)
    a.append(a[0])
    a=a[1:]

# еще решение через строки
# n,m=map(int,input().split())
# a=''
# for j in range(1, m + 1):
#     a += str(j).ljust(3)
# print(a)
# for i in range(n-1):
#     a=a[3:]+a[0:3]
#     print(a)




n,m=map(int,input().split())
a=[[1]*m for i in range(n)]
k=1
for i in range(m):
    for j in range(n):
        a[j][i]=k
        k+=1
# print(a)
for i in a:
    print(*i)
# вар 2(через строки более экономный по памяти)
# n,m=map(int,input().split())
# for i in range(1,n+1):
#     a=str(i).ljust(3)
#     for j in range(1,m):
#         i+=n
#         a+=str(i).ljust(3)
#         if j%m==0:
#             a+='\n'
#     print(a)
# еще решение
# n, m = (int(i) for i in input().split())
# [print(*[str(r + n * c).ljust(2) for c in range(m)]) for r in range(1, n + 1)]




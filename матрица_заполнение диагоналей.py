n,m=map(int,input().split())
count=0
a=[[1]*m for i in range(n)]
for l in range(m+n+1):
    for i in range(n):
        for j in range(m):
            if i+j==l:
                count+=1
                a[i][j]=str(count).ljust(2)
for i in a:
    print(*i)

# вар 2
# n, m = [int(x) for x in input().split()]
# l = [[0] * m for _ in range(n)]
# k = 1
# for j in range(m + n):
#     for i in range(n):
#         if 0 <= j - i < m:
#             l[i][j - i] = k
#             k += 1
# for i in range(n):
#     print(*l[i])
# еще решение через строки(не совсем правильное)
# n,m=map(int,input().split())
# count=0
# a=''
# for l in range(m+n+1):
#
#     for i in range(n):
#
#         for j in range(m):
#             if i+j==l:
#                 count+=1
#                 a+=str(count).ljust(3)
#             else:
#                 a+=' '
#         a+='\n'
# print(a)





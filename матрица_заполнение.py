n,m=map(int,input().split())
a=''
for i in range(1,n*m+1):
    a+=str(i).ljust(3)
    if i%m==0:
        a+='\n'
print(a)
# еще решение
# n, m = map(int, input().split())
# [print(*(str(i * m + j).ljust(3) for j in range(1, m + 1))) for i in range(n)]




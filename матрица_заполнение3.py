n=int(input())
a=''
for i in range(n):
    for j in range(n):
        if j==n-i-1 or i==j:
            a+=str(1).ljust(3)
        else:
            a+=str(0).ljust(3)
    a+='\n'
print(a)

# через списки
# n=int(input())
# for i in range(n):
#     a=[]
#     for j in range(n):
#         if j==n-i-1 or i==j:
#             a.append(1)
#         else:
#             a.append(0)
#     print(*a)
# еще решение
# (lambda n=int(input()): [print(*[str(int(i==j or i==n-j-1)).ljust(3) for j in range(n)]) for i in range(n)])()



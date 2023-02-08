n,m=map(int,input().split())
for i in range(n):
    a1=[]
    if i%2==0:
        for j in range(m):
            if j%2==0:
                a1.append('.')
            else:
                a1.append('*')
    if i%2!=0:
        for j in range(m):
            if j%2==0:
                a1.append('*')
            else:
                a1.append('.')
    print(*a1)
# еще решение
# pos = [int(i) for i in input().split()]
# for i in range(pos[0]):
#     for j in range(pos[1]):
#         if i % 2 == j % 2:
#             print('.', end = ' ')
#         else:
#             print('*', end = ' ')
#     print()




# Программа должна вывести указанную таблицу с замененными столбцами.
n=int(input())
cont=[i for i in range(1,n**2+1,1)]
# print(cont)
a=[list(map(int,input().split())) for i in range(n)]
summ=sum(a[0])
s=True
a1=[]
a2=[]
c1=[]
for i in range(n):
    c = []
    for j in range(n):
        if a[i][j] in c1 or a[i][j] not in cont:
            s=False
            break
        c.append(a[j][i])
        c1.append(a[i][j])
        if i==j:
            a1.append(a[i][j])
        if j==n - i - 1:
            a2.append(a[i][j])
    if sum(c) != summ:
        s = False
        break
if (sum(a1) and sum(a2))!=summ:
    s=False
for i in a:
    if sum(i)!=summ:
        s=False
        break
if s:
    print('YES')
else:
    print('NO')

# еще решение
# n = int(input())
# a = [[*map(int, input().split())] for _ in range(n)]
# print(('NO', 'YES')[set(sum(a, [])) == set((*range(1, n ** 2 + 1),))   # ряд натур. чисел до n ** 2
#                     and
#                     len(set(map(sum, (*a,                              # суммы строк
#                                   *zip(*a),                            # суммы столбцов (транспон-ый кв-т)
#                                   [a[i][i] for i in range(n)],         # сумма гл. диагоналей
#                                   [a[i][~i] for i in range(n)]))       # сумма втор. диагонали
#                        )) == 1])                                       # все они должны совпадать




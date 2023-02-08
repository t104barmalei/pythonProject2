# матрица_ходы коня
n=int(input())
sh=[['.']*n for i in range(8)]
# for i in sh:
#     print(i)
for i in range(n):
    for j in range(n):
        # if i==j:
        #     sh[i][j]=0
        sh[i][j]=abs(j-i)
    print(*sh[i])









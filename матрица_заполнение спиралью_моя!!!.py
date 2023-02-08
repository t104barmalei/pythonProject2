n,m=map(int,input().split())
count=1
mas=[[0]*m for i in range(n)]
d_row=d_column=0
d_row_1=n
d_column_1=m
while count<m*n:
    for i in range(d_column,d_column_1):
        if count > m * n:
            break
        mas[d_row][i]=count
        count+=1
    d_row+=1
    for i in range(d_row,d_row_1):
        if count > m * n:
            break
        mas[i][d_column_1-1]=count
        count+=1
    d_column_1-=1
    for i in range(d_column_1-1,d_column-1,-1):
        if count > m * n:
            break
        mas[d_row_1-1][i]=count
        count+=1
    d_column+=1
    d_row_1-=1
    for i in range(d_row_1-1,d_row-1,-1):
        if count > m * n:
            break
        mas[i][d_column-1]=count
        count+=1
for row in mas:
    for elem in row:
        print(str(elem).rjust(len(str(n * m))),end=' ')
    print()

# еще решение через приросты
# n, m = map(int, input().split())
# arr = [[0]*m for i in range(n)]
#
# x, y, dx, dy = 0, 0, 0, 1
# for i in range(n*m):
#     arr[x][y] = i + 1
#     if arr[(x + dx) % n][(y + dy) % m]!=0:
#         dx, dy = dy, -dx
#     x, y = x + dx, y + dy
#
# for row in arr:
#     print(*row)




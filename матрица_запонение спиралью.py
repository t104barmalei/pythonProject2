n,m=map(int,input().split())
x=0
y=-1
i=1
mas=[[0]*m for i in range(n)]
d_row=0
d_column=1
while i<=n*m:
    if  0<=x+d_row<n and 0<=y+d_column<m and  mas[x+d_row][y+d_column]==0:
        x+=d_row
        y+=d_column
        mas[x][y]=i
        i+=1
    else:
        if d_column==1:
            d_row=1
            d_column=0
        elif d_row==1:
            d_row=0
            d_column=-1
        elif d_column==-1:
            d_column=0
            d_row=-1
        elif d_row==-1:
            d_row=0
            d_column=1
for row in mas:
    for elem in row:
        print(str(elem).rjust(len(str(n**2))),end=' ')
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




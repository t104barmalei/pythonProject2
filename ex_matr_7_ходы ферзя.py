# матрица_ходы ферзя (решение через строки)
xy=input()
sh=[['.']*8 for i in range(8)]
for i in range(8,0,-1):
    a=''
    for j in range(8):
        if int(xy[1])-i==0 and ord(xy[0])-97-j==0:
            a+=' Q'
        elif abs(ord(xy[0])-97 - j) == abs(int(xy[1]) - i) or int(xy[1]) == i or ord(xy[0])-97==j:
            a+=' *'
        else:
            a+=' .'
    print(a)

# решение через списки
# xy=input()
# sh=[['.']*8 for i in range(8)]
# for i in range(8,0,-1):
#     for j in range(8):
#         if int(xy[1])-i==0 and ord(xy[0])-97-j==0:
#             sh[abs(i-8)][j]=' Q'
#         elif abs(ord(xy[0])-97 - j) == abs(int(xy[1]) - i) or int(xy[1]) == i or ord(xy[0])-97==j:
#             sh[abs(i-8)][j]=' *'
#         else:
#             sh[abs(i-8)][j]=' .'
# for i in sh:
#     print(*i)









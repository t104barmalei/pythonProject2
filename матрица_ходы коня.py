# матрица_ходы коня
xy=input()
for i in range(8,0,-1):
    a=''
    for j in range(8):
        if (ord(xy[0])-97-j)**2+(int(xy[1])-i)**2==5:
            a+=' *'
        elif int(xy[1])-i==0 and ord(xy[0])-97-j==0:
            a+=' N'
        else:
            a+=' .'
    print(a)

# еще решение
#





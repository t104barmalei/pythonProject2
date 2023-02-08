Timur=input()
Ruslan=input()
Спок=['камень','ножницы']
ножницы=('бумага','ящерица')
камень=('ножницы','ящерица')
бумага=('камень','Спок')
ящерица=('Спок','бумага')
if Timur==Ruslan:
    print('ничья')
elif Ruslan in Спок and Timur=='Спок':
    print('Тимур')
elif Timur=='камень' and Ruslan in камень:
    print('Тимур')
elif Timur=='ножницы' and Ruslan in ножницы:
    print('Тимур')
elif Timur=='ящерица' and Ruslan in ящерица:
    print('Тимур')
elif Timur=='бумага' and Ruslan in бумага:
    print('Тимур')
else:
    print('Руслан')





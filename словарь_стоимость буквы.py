a={1:	('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'),
2:	('D', 'G'),
3:	('B', 'C', 'M', 'P'),
4:	('F', 'H', 'V', 'W', 'Y'),
5:	('K'),
8:	('J', 'X'),
10:	('Q', 'Z')}
b=input()
c=[]
count=0
for i in b:
    for key,value in a.items():
        if i in value:
            count+=key
print(count)

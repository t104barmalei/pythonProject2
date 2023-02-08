cod=input()
a={}
for i in range(int(input())):
    b=input().split(':')
    # a[int(b[1].strip())]=b[0]
    a.setdefault(int(b[1].strip()),b[0])
c=''
for i in cod:
    c+=a.get(cod.count(i))
print(cod)
print(a)
print(c)
# # input_data
# *!*!*?
# 3
# а: 3
# н: 2
# с: 1
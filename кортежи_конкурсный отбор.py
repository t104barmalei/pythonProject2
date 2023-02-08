n=int(input())
a=[input().split() for i in range(n)]
b=[]
for i in a:
    print(*i)
    if i[1] in ['4','5']:
        b.append(i)
print()
for i in b:
    print(*i)
# еще решение
# students = [tuple(input().split()) for _ in range(int(input()))]
# for student in students:
#     print(*student)
# print()
# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)






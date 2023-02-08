colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']
# a=[]
# for i in colors:
#     for j in sizes:
#         a.append((i,j))
# print(a)

print([(i,j) for i in colors for j in sizes])
a1={}
for i in range(int(input())):
    a,b,c=map(str,input().split())
    a1[a]=a1.setdefault(a,{b:0})
    if b not in a1[a]:
        a1[a].update({b:int(c)})
    else:
        a1[a][b]=a1[a].get(b)+int(c)
print(a1)
for i in sorted(a1):
    print(i+':')
    for key,value in sorted(a1[i].items()):
        print(key,value)

# # еще решение
# sp = [(a,b,int(c)) for a,b,c in [input().split() for _ in range(int(input()))]]
# dc = {}
# for a,b,c in sp:
#   if a not in dc:
#     dc[a] = dc.setdefault(a, {b : c})
#   elif b not in dc[a]:
#     dc[a].update({b : c})
#   else:
#     dc[a][b] = dc[a].get(b) + c
# for k,v in sorted(dc.items()):
#     print(k+':')
#     for x,y in sorted(v.items()):
#         print(x,y)

#  программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.

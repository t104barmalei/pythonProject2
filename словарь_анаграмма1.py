a=input().lower()
a1={i:a.count(i) for i in a if i not in '.,!?:;- '}
b=input().lower()
b1={i:b.count(i) for i in b if i not in '.,!?:;- '}
if sorted(a1)==sorted(b1) and sorted(a1.values())==sorted(b1.values()):
    print("YES")
else:
    print("NO")
# print(a)
# print(b)
# print(sorted(a1))
# print(sorted(b1))
# print(sorted(a1.values()))
# print(sorted(b1.values()))
# # еще решение
# d1,d2={},{}
# for c in input().lower():
#     if c.isalpha():
#         d1[c]=d1.get(c,0)+1
# for c in input().lower():
#     if c.isalpha():
#         d2[c]=d2.get(c,0)+1
# print('YES' if d1==d2 else 'NO')
a=input()
a1={i:a.count(i) for i in a}
b=input()
b1={i:b.count(i) for i in b}
if sorted(a)==sorted(b) and sorted(a1.values())==sorted(b1.values()):
    print("YES")
else:
    print("NO")
# print(a1)
# print(b1)

# # еще решение
# dict1, dict2 = {}, {}
# for i in input():
#     dict1[i] = dict1.setdefault(i, 0) + 1
# for i in input():
#     dict2[i] = dict2.setdefault(i, 0) + 1
# print('YES' if dict1 == dict2 else 'NO')

# вар2
# d1 = {}
# d2 = {}
# for c in input():
#     d1[c] = d1.get(c, 0) + 1
# for c in input():
#     d2[c] = d2.get(c, 0) + 1
# print(['NO', 'YES'][d1 == d2])
#
# # вар3
# string1, string2 = input(), input()
# word1 = {i: string1.count(i) for i in string1}
# word2 = {i: string2.count(i) for i in string2}
# print('YES' if word1 == word2 else 'NO')
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
for i in dict1:
    if i in dict2:
        result[i]=dict1[i]+dict2[i]
        dict2.pop(i)
dict1.update(dict2)
dict1.update(result)
result=dict1.copy()
print(result)



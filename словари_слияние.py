def merge(values):      # values - это список словарей
    a={}
    for i in values:
        for key,value in i.items():
            a.setdefault(key,set()).add(value)
    return(a)




print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

# Следующий программный код:
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# создает словарь:
# result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# a.setdefault(a1[1], []).append(a1[0])
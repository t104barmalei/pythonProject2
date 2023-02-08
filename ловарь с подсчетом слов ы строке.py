def get_word_indices(s):
    """необходимо создать функцию get_word_indices, которая принимает список строк и возвращает словарь,
    где ключи - это уникальные слова из списка строк в нижнем регистре, а значения - это списки индексов строк,
     в которых эти слова встречаются."""
    s1={}
    for i in range(len(s)):
        for j in range(len(s[i].split())):
            x=s[i].split()[j].lower()
            s1.setdefault(x,[]).append(i)
            # или так
            # if x in s1:
            #     x2=s1.setdefault(x)
            #     x2.append(i)
            # else:
            #     s1.setdefault(x, [i])
    return s1

# еще решение
# def get_word_indices(strings: list[str]) -> dict:
#     d = {}
#     for i, k in enumerate(strings):
#         for j in k.lower().split():
#             d.setdefault(j, []).append(i)
#     return d

print(get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']))
print(get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']))
print(get_word_indices([]))
print(get_word_indices(['Avada Kedavra',
                         'avada kedavra',
                         'AVADA KEDAVRA']))



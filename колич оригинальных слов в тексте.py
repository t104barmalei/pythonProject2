# определение общего количества различных слов в строке текста без учета знаков препинания
print(len(set([i.strip('.,;:-?!') for i in list(map(str,input().lower().split()))])))
def process(sentences):
    result = []
    for i in sentences:
        a1=''
        for j in i.split():
            if j.isalpha():
                a1+=j+' '
        result.append(a1.strip())
    return result

print(process(['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']))

# sentences='1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888'
# sentences=list(sentences)
# print(sentences)

















s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate ' \
    'barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot ' \
    'currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant ' \
    'orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# a={}
# for i in s.split():
#     a[i]=s.split().count(i)
a={i:s.split().count(i) for i in s.split()}
# print(a)
a1=[]
for i in a:
    if a.get(i)==max(a.values()):
        a1.append(i)
# print(a)
# print(max(a.values()))
print(min(a1))
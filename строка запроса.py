def build_query_string(params):
    a=[]
    for key,value in params.items():
        a.append(key+'='+str(value))
    stroka='&'.join(sorted(a))
    return(stroka)

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
# age=28&name=timur
# game=2&sport=hockey&time=17
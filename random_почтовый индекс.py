from random import *
def generate_index():
    a=''
    while len(a)<9:
        if len(a)<2 or len(a)>=7:
            b=randint(65,90)
            a+=chr(b)
        elif 2<=len(a)<4 or 5<=len(a)<7:
            b = randint(0, 9)
            a+=str(b)
        elif len(a)==4:
            a+='_'

    return a

print(generate_index())


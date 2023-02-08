from random import *
def generate_ip():
    a=[]
    while len(a)<4:
        b=randint(0,255)
        if b not in a:
            a.append(str(b))
    ip='.'.join(a)
    return ip

print(generate_ip())


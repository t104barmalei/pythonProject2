a={'write':'W','read':'R','execute':'X'}
b=int(input())
a1={}
for i in range(b):
    c=input().split()
    a1[c[0]]=tuple(c[1:])
print(a1)
for i in range(int(input())):
    c1=input().split()
    if a[c1[0]] in a1[c1[1]]:
        print('OK')
    else:
        print('Access denied')

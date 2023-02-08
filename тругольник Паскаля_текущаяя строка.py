def factorial(a):
    pr=1
    for i in range(1,a+1):
        pr*=i
    return pr

n=int(input())
sp=[]
for i in range(n+1):
    sp.append(int(factorial(n)/(factorial(i)*factorial(n-i))))
print(sp)



















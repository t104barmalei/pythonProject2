def factorial(a):
    pr=1
    for i in range(1,a+1):
        pr*=i
    return pr

n=int(input())
for j in range(n):
    sp=[]
    for i in range(j+1):
        sp.append(int(factorial(j)/(factorial(i)*factorial(j-i))))
    print(sp)


















str= input().split()
n=int(input())
a=[]
for i in range(n):
    a1=[]
    str1=str[i:]
    for j in range(len(str1)):
        if j%n==0:
            a1.append(str1[j])
    a.append(a1)
print(a)



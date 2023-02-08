n=int(input())
a=''
for i in range(n):
    for j in range(n):
        if j==n-i-1 or i==j or (i<n-1-j and i<j) or (i>n-1-j and i>j):
            a+=str(1).ljust(3)
        else:
            a+=str(0).ljust(3)
    a+='\n'
print(a)

# еще решение




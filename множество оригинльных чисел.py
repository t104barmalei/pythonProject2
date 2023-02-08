a= list(map(int,input().split()))
a1=set()
for i in a:
    if i not in a1:
        print("NO")
    else:
        print("YES")
    a1.add(i)
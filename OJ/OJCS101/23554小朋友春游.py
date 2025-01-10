n=int(input())
l=list(map(int,input().split()))
l.sort()
a=list(range(1,n+1))
b=[]
for i in l:
    if i<=n:
        a.remove(i)
    else:
        b.append(i)
print(*a)
print(*b)

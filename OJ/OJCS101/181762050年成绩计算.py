import math
zhi=[]
m,n=map(int,input().split())
sty=10**4+1
eur=[True]*(sty)
for i in range(2,sty):
    if eur[i]:
        for j in range(i*i,sty,i):
            eur[j]=False

for i in range(m):
    xi=list(map(int,input().split()))
    ans=0
    n=len(xi)
    for x in xi:
        q=math.sqrt(x)
        if q==int(q):
            if eur[int(q)]:
                ans+=x
    if ans==0:
        print(0)
    else:
        ans=ans/n
        print(f'{ans:.2f}')


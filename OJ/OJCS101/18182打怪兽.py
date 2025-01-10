nc=int(input())
for i in range(nc):
    n,m,b=map(int,input().split())
    tx={}
    for i in range(n):
        ti,xi=map(int,input().split())
        if ti in tx.keys():
            tx[ti].append(xi)
        else:
            tx[ti]=[xi]
    t=list(tx.keys())
    t.sort()
    for i in range(len(t)):
        a=tx[t[i]]
        long=len(a)
        if long>=m:
            long=m
        a.sort(reverse=True)
        db=sum(a[i] for i in range(long))
        b-=db
        if b<=0:
            print(t[i])
            break
    if b>0:
        print('alive')




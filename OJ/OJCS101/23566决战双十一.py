n,m=map(int,input().split())
sp={}
qx={}
for i in range(n):
    si,pi=map(int,input().split())
    if si in sp.keys() :
        sp[si].append(pi)
    else:
        sp[si]=[pi]
for j in range(m):
    qx0=input()
    xm=qx0.index('-')
    q,x=int(qx0[:xm]),int(qx0[xm+1:])
    qx[j+1]=(q,x)
ans=sum(sum(sp[i]) for i in range(1,m+1))
ans-=(ans//200)*30
for i in range(1,m+1):
    p=sum(sp[i])
    if qx[i][0]<=p:
        ans-=qx[i][1]
print(ans)




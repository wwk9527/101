n,m=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
a=[]
for i in range(1,n):
    a.append((i,r[i]-r[i-1]))
a.sort(key=lambda x:x[1],reverse=True)
t=sum(a[i][1] for i in range(m-1,n-1))
print(t)



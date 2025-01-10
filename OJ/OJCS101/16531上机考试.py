m,n=map(int,input().split())
mp=[list(map(int,input().split())) for i in range(m)]
haxi={}
for i in range(m):
    for j in range(n):
        haxi[mp[i][j]]=(i,j)
youx={}
for i in range(n*m):
    v=list(map(int,input().split()))
    gra=0
    for x in v:
        if x==1:
            gra+=1
    mp[haxi[i][0]][haxi[i][1]]=v
    if gra in youx.keys():
        youx[gra]+=1
    else:
        youx[gra]=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
xito=set()
for i in range(m):
    for j in range(n):
        for k in range(4):
            if 0<=i + dx[k] <m and 0<= j + dy[k]<n:
                if mp[i][j]==mp[i+dx[k]][j+dy[k]]:
                    xito.add((i,j))
a=list(youx.keys())
a.sort(reverse=True)
tol=n*m
z=0
for x in a:
    if z+youx[x]>0.4*tol:
        break
    else:
        z=z+youx[x]
print(len(xito),z)


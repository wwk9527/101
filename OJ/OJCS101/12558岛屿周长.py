n,m=map(int,input().split())
mp=[[0]*(m+2) ]
for i in range(n):
    a=list(map(int,input().split()))
    a.append(0)
    mp.append([0]+a)
mp.append([0]*(m+2))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if mp[i][j]==1 :
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                if mp[x][y]==0 :
                    count+=1
print(count)



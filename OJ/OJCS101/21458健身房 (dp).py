T,n=map(int,input().split())
a=[]
for k in range(n):
    a.append(list(map(int,input().split())))
a.sort()
dp=[[0,[]] for _ in range(T+1)]
for _ in range(n):
    dp[a[_][0]][0]=a[_][1]
    dp[a[_][0]][1]=[_]
for i in range(1,T+1):
    if dp[i][0]!=0:
        for j in range(n):
            if j not in dp[i][1] and i+a[j][0]<=T and dp[i+a[j][0]][0]<dp[i][0]+a[j][1]:
                dp[i+a[j][0]][0]=dp[i][0]+a[j][1]
                dp[i+a[j][0]][1]=dp[i][1]+[j]
if dp[-1][1]==[]:
    print(-1)
else:
    print(dp[-1][0])


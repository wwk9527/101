g=[1,2,3,5,10,20]
num=list(map(int,input().split()))
su=sum(num[i]*g[i] for i in range(6))
dp=[0]*1001
dp[0]=1
for a1 in range(num[0]+1):
    for a2 in range(num[1] + 1):
        for a3 in range(num[2] + 1):
            for a4 in range(num[3] + 1):
                for a5 in range(num[4] + 1):
                    for a6 in range(num[5] + 1):
                        d=a1*g[0]+a2*g[1]+a3*g[2]+a4*g[3]+a5*g[4]+a6*g[5]
                        dp[d]=1
ans=dp.count(1)-1
print(f'Total={ans}')
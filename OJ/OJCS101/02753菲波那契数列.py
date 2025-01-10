n=int(input())
dp=[1,1]
for i in range(2, 20):
    dp.append(dp[i - 1] + dp[i - 2])
for i in range(1,n+1):
    a=int(input())
    print(dp[a-1])


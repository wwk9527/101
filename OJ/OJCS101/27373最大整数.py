m=int(input())
n=int(input())
num=list(input().split())
nums=[(len(num[i]),num[i]) for i in range(n)]
nums.sort(key=lambda x: (-x[0],x[1]),reverse=True)
dp=0
for j in range(n):
        for i in range(m,0,-1)


for i in range(m-1,-1,-1):
    if dp[i]!=0:
        print(dp[i])
        break





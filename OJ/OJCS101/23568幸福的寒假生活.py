def date_to_index(date):
    month,day=map(int,date.split('.'))
    return (month-1)*31+day-6
data=[]
dp=[0]*46
n=int(input())
for _ in range(n):
    start,end,happiness=input().split()
    start,end,happiness=date_to_index(start),date_to_index(end),int(happiness)
    data.append((start,end,happiness))
for i in range(1,46):
    dp[i]=dp[i-1]
    for start,end,happiness in data:
        if end==i:
            dp[i]=max(dp[i],dp[start-1]+happiness)
print(dp[-1])



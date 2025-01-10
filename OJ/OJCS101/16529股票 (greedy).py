'''N=int(input())
na=list(map(float,input().split()))
ju=[(i,na[i]) for i in range(N)]
ju.sort(key=lambda x:-x[1])
ans=1
for i in range(N):
    for j in range(N-1,-1,-1):
        if ju[i][0]>ju[j][0]:
            ans=max(ans,ju[i][1]/ju[j][1])
            break
print(f'{ans*100:.2f}')'''#半贪不贪
N=int(input())
na=list(map(float,input().split()))
dp=1
mi=float('inf')
for x in na:
    mi=min(x,mi)
    dp=max(dp,x/mi)
print(f'{dp*100:.2f}')


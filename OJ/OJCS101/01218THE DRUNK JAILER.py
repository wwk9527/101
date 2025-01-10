t=int(input())
for i in range(t):
    n=int(input())
    ans=[1]*n
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j*i <=n:
                ans[i*j-1]*=-1
            else:
                break
    an=ans.count(-1)
    print(an)
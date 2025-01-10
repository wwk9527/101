n=int(input())
md={1:31,2:28,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30}
for i in range(1,n+1):
    m1,d1,x,m2,d2=map(int,input().split())
    ans=0
    if m1==m2:
        ans=d2-d1
    else:
        for i in range(m1, m2 + 1):
            if i == m1:
                ans += md[i] - d1
            elif i == m2:
                ans += d2
            else:
                ans += md[i]
    ans=x*(2**ans)
    print(ans)

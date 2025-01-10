p=int(input())
s=list(map(int,input().split()))
s.sort()
t=0
m=len(s)-1
if p<s[0]:
    print(0)
else:
    while t<m:
        if p-s[t]>=0:
            p -= s[t]
            t+=1
        else:
            p += s[m]
            m-=1

    if p - s[t] >= 0:
        t += 1
        p -= s[t]
    m=len(s)-1-m
    num=t-m
    print(num)


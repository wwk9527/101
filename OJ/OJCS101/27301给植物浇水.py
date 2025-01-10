n,a,b=map(int,input().split())
water=list(map(int,input().split()))
water1=water.copy()
i=0
j=n-1
tak=a
tbk=b
ans=0
while i<=j:
    if i<j:
        if tak < water[i]:
            tak = a
            ans += 1
        if tbk < water[j]:
            tbk = b
            ans += 1
        tak -= water[i]
        tbk -= water[j]
        i+=1
        j-=1
    else:
        if tak>=tbk:
            if tak < water[i]:
                tak = a
                ans += 1
                break
            else :
                break
        else:
            if tbk < water[j]:
                tbk = b
                ans += 1
                break
            else:
                break
print(ans)



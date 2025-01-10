n=int(input())
ans=0
for i in range(1,n+1):
    if i%7==0 or '7'in str(i):
        ans=ans+0
    else:
        ans=ans+i**2
print(ans)
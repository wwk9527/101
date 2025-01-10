import math
s=input()
n=len(s)
m=math.floor(math.log(n,2))
ans=[]
for i in range(m+1):
    ans.append(s[2**i-1])
i=0
j=m
ans1=[]
while i<=j:
    if i==j:
        ans1.append(ans[i])
    else:
        ans1.append(ans[i])
        ans1.append(ans[j])
    i+=1
    j-=1
print(''.join(ans1))




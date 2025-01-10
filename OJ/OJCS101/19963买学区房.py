import re


n=int(input())

data=input()
# 使用正则表达式查找所有的数字
xy = [int(num) for num in re.findall(r'\d+', data)]
val=list(map(int,input().split()))
xing=[]
for i in range(1,n+1):
    d=xy[2*(i-1)]+xy[2*i-1]
    xing.append((d/val[i-1],val[i-1]))
xing.sort(key=lambda x:-x[0])
xin=xing.copy()
xin.sort(key=lambda x:x[1])
vban=0
if n%2==0:
    vban=(xin[n//2-1][1]+xin[n//2][1])/2
    db=(xing[n//2-1][0]+xing[n//2][0])/2
else:
    vban=xin[n//2][1]
    db=xing[n // 2 ][0]
ans=0
for i in range(n//2):
    if xing[i][1]<vban and xing[i][0] >db:
        ans+=1
print(ans)
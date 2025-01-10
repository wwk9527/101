n=int(input())
q=n
i=2
ans=[]
while q>1:
        if q%i==0:
            q//=i
            ans.append(i)
            i=2
        else:
            i+=1
if len(set(ans))==len(ans):
    if len(ans)%2==0:
        print(1)
    else:
        print(-1)
else:
    print(0)
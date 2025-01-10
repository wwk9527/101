matick=[list(map(int,input().split())) for i in range(5)]
ans=[]
ro=[]
co=[]
for i in range(5):
    b=max(matick[i])
    j=matick[i].index(b)
    a=float('inf')
    for k in range(5):
        a=min(a,matick[k][j])
    if matick[i][j]==a:
        ans.append(i+1)
        ans.append(j+1)
        ans.append(b)
if len(ans)==0:
    print("not found")
else:
    print(' '.join(str(j) for j in ans) )



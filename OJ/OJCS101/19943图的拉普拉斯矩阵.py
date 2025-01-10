n,m=map(int,input().split())
mp={}
L=[[0 for _ in range(n)] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    L[a][b]=-1
    L[b][a]=-1
    if a in mp.keys():
        mp[a].append(b)
    else:
        mp[a]=[b]
    if b in mp.keys():
        mp[b].append(a)
    else:
        mp[b]=[a]
for i in mp.keys():
    L[i][i]=len(mp[i])
for x in L:
    print(' '.join(str(i) for i in x))



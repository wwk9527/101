def dfs(start,bian,visit,depth):
    if depth>=l:
        return
    visit.add(start)
    for i in dis[start]:
        if i not in ans and i not in visit:
            ans.append(i)
            dfs(i,bian,visit,depth+1)
    visit.remove(start)

n,m,l=map(int,input().split())
bian=[list(map(int,input().split())) for i in range(m)]
dis={}
for i in  bian:
    if i[0] not in dis.keys():
        dis[i[0]]=[i[1]]
    else:
        dis[i[0]].append(i[1])
    if i[1] not in dis:
        dis[i[1]]=[i[0]]
    else:
        dis[i[1]].append(i[0])
    dis[i[0]].sort()
    dis[i[1]].sort()
start=int(input())
visit=set()
ans=[start]
if start not in dis.keys():
    print(start)
else:
    dfs(start,bian,visit,0)
    print(*ans)






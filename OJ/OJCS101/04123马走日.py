dx=[1,-1,2,-2,1,-1,2,-2]
dy=[2,2,1,1,-2,-2,-1,-1]
def dfs(x,y,con,ans):
    visit.add((x,y))
    if len(visit)==n*m:
        con[0]+=1
        visit.remove((x, y))
        return
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and (nx,ny) not in visit :
            dfs(nx,ny,con,ans+1)
    visit.remove((x,y))
t=int(input())
for i in range(t):
    n, m, x, y = map(int, input().split())
    visit = set()
    con = [0]
    dfs(x,y,con,0)
    print(con[0])

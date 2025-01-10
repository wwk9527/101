'''dx=[0,0,1,-1]
dy=[1,-1,0,0]
m,n,p=map(int,input().split())
def dfs(x,y,s,t,dp,cnt):
    if x == s and y == t:
        dp.append(cnt)
        cnt=0
        return

    visited[x][y] = True

    # 遍历四个方向
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 检查新坐标是否在边界内、未访问过，并满足某些条件
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            if grid[nx][ny]=='#':
                cut=0
                continue
            new_cnt = cnt + abs(int(grid[nx][ny]) - int(grid[x][y]))
            dfs(nx, ny, s, t, dp, new_cnt)

    # 回溯时取消访问标记
    visited[x][y] = False


grid=[]
for i in range(m):
    a=input().split()
    b=[]
    for j in range(n):
        if a[j]=='#':
            b.append(a[j])
        else:
            b.append(int(a[j]))
    grid.append(b)

for i in range(p):
    visited = [[False] * n for i in range(m)]
    x,y,s,t=map(int,input().split())
    if grid[x][y]=='#':
        print('NO')
    else:
        dp=[]
        cnt=0
        dfs(x,y,s,t,dp,cnt)
        if len(dp)==0:
            print('NO')
        else:
            print(min(dp))'''
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n, p = map(int, input().split())

grid = []
for i in range(m):
    a = input().split()
    grid.append([int(x) if x != '#' else '#' for x in a])


def dijkstra(x, y, s, t):
    if grid[x][y] == '#':
        return float('inf')  # 不可到达

    min_cost = [[float('inf')] * n for _ in range(m)]
    min_cost[x][y] = 0
    pq = []
    heapq.heappush(pq, (0, x, y))  # (cost, x, y)

    while pq:
        current_cost, cx, cy = heapq.heappop(pq)

        if (cx, cy) == (s, t):
            return current_cost

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                new_cost = current_cost + abs(int(grid[nx][ny]) - int(grid[cx][cy]))

                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return float('inf')  # 无法到达目标


for i in range(p):
    x, y, s, t = map(int, input().split())
    result = dijkstra(x, y, s, t)
    if result == float('inf'):
        print('NO')
    else:
        print(result)





from collections import deque

def bfs(R, C, K, grid):
    # 找到起点和终点
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    # 初始化队列和访问标记
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = [[set() for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]].add(0)

    # 方向数组
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, time = queue.popleft()

        # 如果到达终点
        if (x, y) == end:
            return time

        # 计算下一个时间
        next_time = time + 1

        # 遍历四个方向
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 检查新坐标是否在边界内
            if 0 <= nx < R and 0 <= ny < C:
                # 如果当前时间是 K 的倍数，可以走到石头位置
                if next_time % K == 0:
                    if (nx, ny) not in visited[nx][ny] or next_time not in visited[nx][ny]:
                        visited[nx][ny].add(next_time)
                        queue.append((nx, ny, next_time))
                # 否则只能走到非石头位置
                elif grid[nx][ny] != '#':
                    if (nx, ny) not in visited[nx][ny] or next_time not in visited[nx][ny]:
                        visited[nx][ny].add(next_time)
                        queue.append((nx, ny, next_time))

    # 如果无法到达终点
    return "Oop!"

# 读取输入
T = int(input())
for _ in range(T):
    R, C, K = map(int, input().split())
    grid = [input().strip() for _ in range(R)]
    result = bfs(R, C, K, grid)
    print(result)



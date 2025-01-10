def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 'W':
        return 0

    # 标记已访问
    grid[i][j] = '.'

    size = 1
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = i + dx, j + dy
            size += dfs(grid, nx, ny)

    return size


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    max_area = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                area = dfs(grid, i, j)
                max_area = max(max_area, area)

    print(max_area)




def dfs(x, y):
    # 如果该位置已经计算过最长路径，则直接返回
    if memo[x][y] != 0:
        return memo[x][y]

    max_length = 1  # 每个点至少可以滑行1步，即停在原地

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 检查是否越界以及新位置的高度是否小于当前位置
        if 0 <= nx < r and 0 <= ny < c and mich[nx][ny] < mich[x][y]:
            length = 1 + dfs(nx, ny)
            max_length = max(max_length, length)

    memo[x][y] = max_length
    return max_length

# Directions for moving up, down, left, right
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Read input
r, c = map(int, input().split())
mich = [list(map(int, input().split())) for _ in range(r)]

# Initialize memoization table
memo = [[0] * c for _ in range(r)]

# Calculate the longest ski slope
max_slope_length = 0
for i in range(r):
    for j in range(c):
        max_slope_length = max(max_slope_length, dfs(i, j))

print(max_slope_length)

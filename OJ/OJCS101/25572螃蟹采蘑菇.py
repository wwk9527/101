# 方向数组，表示四个方向的移动
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_start_and_end(mat):
    start_positions = []
    end_position = None
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 5:
                start_positions.append((i, j))
            elif mat[i][j] == 9:
                end_position = (i, j)
    return start_positions, end_position

def dfs(start1, start2, end):
    stack = [(start1, start2)]
    visit = set()
    visit.add((start1, start2))

    while stack:
        (sx1, sy1), (sx2, sy2) = stack.pop()

        if (sx1, sy1) == end or (sx2, sy2) == end:
            return True

        # 尝试四个方向移动
        for i in range(4):
            nx1, ny1 = sx1 + dx[i], sy1 + dy[i]
            nx2, ny2 = sx2 + dx[i], sy2 + dy[i]

            # 当前状态的检查
            if (0 <= nx1 < n and 0 <= ny1 < n and
                    0 <= nx2 < n and 0 <= ny2 < n and
                    mat[nx1][ny1] != 1 and mat[nx2][ny2] != 1 and
                    ((nx1, ny1), (nx2, ny2)) not in visit):
                visit.add(((nx1, ny1), (nx2, ny2)))
                stack.append(((nx1, ny1), (nx2, ny2)))

    return False

# 输入迷宫大小
n = int(input())

# 读取迷宫矩阵
mat = [list(map(int, input().split())) for _ in range(n)]

# 获取起点和终点
start_positions, end_position = find_start_and_end(mat)

# 开始DFS搜索
if len(start_positions) == 2:
    r = dfs(tuple(start_positions[0]), tuple(start_positions[1]), end_position)
else:
    r = False

# 打印结果
print("yes" if r else "no")




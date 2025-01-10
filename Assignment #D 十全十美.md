# Assignment #D: 十全十美



Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### 02692: 假币问题



brute force, http://cs101.openjudge.cn/practice/02692

思路：

代码：

```
n = int(input())
for case in range(1, n + 1):
    heav=[]
    ligh=[]
    al=set()
    for i in range(3):
        a = input().split()
        x1 = list(a[0])
        x2 = list(a[1])
        x3 = a[2]
        if x3 == 'even':
            al.update(set(x1+x2))
        elif x3 == 'up':
            heav.append(set(x1))
            ligh.append(set(x2))
        else:
            heav.append(set(x2))
            ligh.append(set(x1))
    u=set(heav[0])
    d=set(ligh[0])
    if len(heav)>1:
        for i in heav:
            u=u.intersection(i)
        for i in ligh:
            d=d.intersection(i)
    d=list(d)
    u=list(u)
    for i in u:
        if i not in al and i not in d:
            print(f'{i} is the counterfeit coin and it is heavy. ')
            break
    for i in d:
        if i not in al and i not in u:
            print(f'{i} is the counterfeit coin and it is light. ')
            break

```



![image-20241217181114149](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241217181114149.png)

### 01088: 滑雪



dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

代码：

```
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
```



![image-20241224022646863](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241224022646863.png)

### 25572: 螃蟹采蘑菇



bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：

代码：

```
from collections import deque

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

def bfs(start1, start2, end):
    queue = deque([(start1, start2)])
    visit = set()
    visit.add((start1, start2))

    while queue:
        (sx1, sy1), (sx2, sy2) = queue.pop()

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
                queue.append(((nx1, ny1), (nx2, ny2)))

    return False

# 输入迷宫大小
n = int(input())

# 读取迷宫矩阵
mat = [list(map(int, input().split())) for _ in range(n)]

# 获取起点和终点
start_positions, end_position = find_start_and_end(mat)

# 开始BFS搜索
if len(start_positions) == 2:
    r = bfs(tuple(start_positions[0]), tuple(start_positions[1]), end_position)
else:
    r = False

# 打印结果
print("yes" if r else "no")

```

![image-20241223232854299](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241223232854299.png)

### 27373: 最大整数



dp, http://cs101.openjudge.cn/practice/27373/

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

### 02811: 熄灯问题



brute force, http://cs101.openjudge.cn/practice/02811

思路：

代码：

```
def press_button(grid, row, col):
    for r, c in [(row, col), (row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if 0 <= r < 5 and 0 <= c < 6:
            grid[r][c] = 1 - grid[r][c]

def solve_lights_out(initial_state):
    # 尝试所有第一行按钮的组合（2^6种）
    for first_row_mask in range(64):  # 从0到63，表示第一行的所有可能组合
        # 复制初始状态并转换为可变列表
        grid = [list(row) for row in initial_state]
        solution = [[0]*6 for _ in range(5)]
        
        # 应用第一行的按钮组合
        for col in range(6):
            if first_row_mask & (1 << col):
                press_button(grid, 0, col)
                solution[0][col] = 1
        
        # 根据第一行的结果处理剩余行
        for row in range(1, 5):
            for col in range(6):
                if grid[row-1][col] == 1:  # 如果上一行的灯是亮的
                    press_button(grid, row, col)
                    solution[row][col] = 1
        
        # 检查最后一行是否全灭
        if all(cell == 0 for cell in grid[-1]):
            return solution
    
    # 如果没有找到解，则返回None
    return None

# 输入读取
import sys
input_data = sys.stdin.read().strip()
lines = input_data.split('\n')
initial_state = [list(map(int, line.split())) for line in lines]

# 解决问题并输出答案
solution = solve_lights_out(initial_state)
if solution is not None:
    for row in solution:
        print(" ".join(str(x) for x in row))
else:
    print("No solution found")
```



![image-20241218164708562](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241218164708562.png)

### 08210: 河中跳房子



binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

代码：

```
l, n, m = map(int, input().split())
mp = [int(input()) for _ in range(n)]
mp.append(l)  # 添加终点
mp.append(0)  # 添加起点
mp.sort()

low, high = 1, l  # 跳跃距离至少为1

while low <= high:
    mid = (low + high) // 2
    removed, last_position = 0, 0
    for i in range(1, len(mp)):
        if mp[i] - mp[last_position] < mid:
            removed += 1
        else:
            last_position = i
        if removed > m:  # 二分查找终止条件
            break

    if removed <= m:  # 包括等于m的情况，因为这是有效的
        low = mid + 1  # 尝试更大的跳跃距离
    else:
        high = mid - 1  # 减小跳跃距离

print(high)
```



![image-20241218164740485](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241218164740485.png)

## 2. 学习总结和收获

学的东西太多了，竞争压力还大，希望老师期末留情，搜索题还是太难了。

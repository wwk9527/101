# Assignment #9: dfs, bfs, & dp



Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by 王玮珂 物院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### 18160: 最大连通域面积



dfs similar, http://cs101.openjudge.cn/practice/18160

思路：

代码：

```
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
```

![image-20241126224032978](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241126224032978.png)

### 19930: 寻宝



bfs, http://cs101.openjudge.cn/practice/19930

思路：

代码：

```
q = []

step = [[0, 1], [1, 0], [-1, 0], [0, -1]]
vis = [[0] * 52 for _ in range(52)]
g = []

m, n = map(int, input().split())
for i in range(m):
    g.append([int(x) for x in input().split()])

def check(x, y):
    if (x < 0 or y < 0 or x >= m or y >= n):
        return False
    if (vis[x][y] or g[x][y] == 2):
        return False
    return True


q.append((0, 0))
head = 0
tail = 1
level = 0
while (head < tail):
    # i = head
    # j = tail
    for k in range(head, tail):
        x, y = q[head]
        head += 1
        if (g[x][y] == 1):
            print(level)
            exit(0)     
        for z in range(4):
            newx = x + step[z][0]
            newy = y + step[z][1]
            if (check(newx, newy)):
                vis[newx][newy] = 1
                q.append((newx, newy))
                tail += 1
    level += 1
print('NO')
```

![image-20241126225949757](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241126225949757.png)

### 04123: 马走日



dfs, http://cs101.openjudge.cn/practice/04123

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

### sy316: 矩阵最大权值路径



dfs, https://sunnywhy.com/sfbj/8/1/316

思路：

代码：

```
def dfs(x, y, now_value):
    global max_value, opt_path
    # 如果到达右下角，更新最大权值和最优路径
    if x == n - 1 and y == m - 1:
        if now_value > max_value:
            max_value = now_value
            opt_path = temp_path[:]
        return
    
    # 标记当前位置为已访问
    visited[x][y] = True
    
    # 尝试向四个方向移动
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            next_value = now_value + maze[next_x][next_y]
            temp_path.append((next_x, next_y))
            dfs(next_x, next_y, next_value)
            temp_path.pop()  # 回溯
    
    # 取消当前位置的访问标记
    visited[x][y] = False

# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 初始化变量
max_value = float('-inf')
opt_path = []
temp_path = [(0, 0)]
visited = [[False] * m for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 从左上角开始DFS搜索
dfs(0, 0, maze[0][0])

# 输出最优路径
for x, y in opt_path:
    print(x + 1, y + 1)
```



![image-20241126230536153](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241126230536153.png)

### LeetCode62.不同路径



dp, https://leetcode.cn/problems/unique-paths/

思路：

代码：

```
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dx = [0, 1]
        dy = [1, 0]

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            cnt = 0
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    cnt += dfs(nx, ny)
            return cnt

        return dfs(0, 0)

# 示例用法
if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 7
    print(sol.uniquePaths(m, n))
```



![image-20241126232734433](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241126232734433.png)

### sy358: 受到祝福的平方



dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：

代码：

```
def is_blessed_id(A):
    # 预处理所有可能的平方数
    squares = set()
    i = 1
    while i * i <= 10**9:
        squares.add(i * i)
        i += 1
    
    # 将数字A转换为数字列表
    digits = list(map(int, str(A)))
    
    # DFS函数，判断是否可以分割成平方数
    def dfs(idx):
        if idx == len(digits):
            return True
        
        num = 0
        for i in range(idx, len(digits)):
            num = num * 10 + digits[i]
            if num in squares:
                if dfs(i + 1):
                    return True
        return False
    
    # 调用DFS函数，判断是否可以分割成平方数
    return "Yes" if dfs(0) else "No"

# 读取输入
A = int(input())
# 输出结果
print(is_blessed_id(A))
```



![image-20241126230429886](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241126230429886.png)

## 2. 学习总结和收获



dfs，bfs还是很难找到思路，决定再看看讲义


# Assignment #C: 五味杂陈



Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### 1115. 取石子游戏



dfs, https://www.acwing.com/problem/content/description/1117/

思路：

代码：

```
def f(i):
    if i % 2 == 0:
        return 'win'
    else:
        return 'lose'
def inf(a,b,i):
    if a%b==0:
        return f(i)
    else:
        if a//b>1:
            return f(i)
        else:
            a,b=b,a%b
            i+=1
            return inf(a,b,i)
while True:
    i=0
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    a,b=max(a,b),min(a,b)
    print(inf(a,b,i))

```

![image-20241212141104861](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241212141104861.png)



### 25570: 洋葱



Matrices, http://cs101.openjudge.cn/practice/25570

遍历就过了，没有难度

代码：

```
n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
if n==1:
    print(m[0][0])
else:
    if n % 2 == 0:
        s = []
        for i in range(n // 2):
            r1 = sum(m[i][j] for j in range(i, n - i))
            r2 = sum(m[n - 1 - i][j] for j in range(i, n - i))
            c1 = sum(m[j][i] for j in range(i, n - i))
            c2 = sum(m[j][n - 1 - i] for j in range(i, n - i))
            s.append(r1 + r2 + c1 + c2 - m[i][i] - m[n - 1 - i][n - 1 - i] - m[i][n - 1 - i] - m[n - 1 - i][i])
        print(max(s))
    else:
        s = [m[(n - 1) // 2][(n - 1) // 2]]
        for i in range((n - 1) // 2):
            r1 = sum(m[i][j] for j in range(i, n - i))
            r2 = sum(m[n - 1 - i][j] for j in range(i, n - i))
            c1 = sum(m[j][i] for j in range(i, n - i))
            c2 = sum(m[j][n - 1 - i] for j in range(i, n - i))
            s.append(r1 + r2 + c1 + c2 - m[i][i] - m[n - 1 - i][n - 1 - i] - m[i][n - 1 - i] - m[n - 1 - i][i])
        print(max(s))
```



![image-20241212143453576](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241212143453576.png)

### 1526C1. Potions(Easy Version)



greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

代码：

```
# 读取输入
n = int(input())
lst = list(map(int, input().split()))

# 初始化动态规划数组
dp = [-1] * (n + 1)
dp[0] = 0  # 不喝任何药水，生命值为0

# 动态规划填充表格
for i in range(n):  # 遍历每一瓶药
    for j in range(i + 1, 0, -1):  # 从后往前更新，避免覆盖当前状态
        if dp[j - 1] >= 0:
            dp[j] = max(dp[j], dp[j - 1] + lst[i])

# 查找可以喝的最大药水数量，使得生命值非负
for k in range(n, -1, -1):
    if dp[k] >= 0:
        print(k)  # 输出结果
        break
```



![image-20241212170050858](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241212170050858.png)

### 22067: 快速堆猪



辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：原来超时然后加了个辅助栈保存最小值，结果一开始只写了n<a[-1]，导致压入相同最小值时会出错，换成n<=a[-1]就对了。但是我不太明白 sys.stdin.readline() 能加快多少？考试的时候有必要用吗？

代码：

```
pig=[]
a=[10000000]
while True:
    try:
        step=input()
        if step=="pop":
            if len(pig)>0:
                if pig[-1]==a[-1]:
                    a.pop()
                pig.pop()

        elif step=="min":
            if len(pig)>0:
                print(a[-1])
        else:
            l=step.split()
            n=int(l[-1])
            pig.append(n)
            if n<=a[-1]:
                a.append(n)
    except:
        break
```

![image-20241212171511403](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241212171511403.png)

### 20106: 走山路



Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

### 04129: 变换的迷宫



bfs, http://cs101.openjudge.cn/practice/04129/

思路：

代码：

```
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
    visited = [[[False] * K for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]][0] = True

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
        next_time_mod = next_time % K

        # 遍历四个方向
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 检查新坐标是否在边界内
            if 0 <= nx < R and 0 <= ny < C:
                # 如果当前时间是 K 的倍数，可以走到石头位置
                if next_time_mod == 0 or grid[nx][ny] != '#':
                    if not visited[nx][ny][next_time_mod]:
                        visited[nx][ny][next_time_mod] = True
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

```



![image-20241212204855367](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241212204855367.png)

## 2. 学习总结和收获



喝药和走山路还有迷宫都是ai帮我优化的，自己写不是超时就是超内存。其他三道题还能自己写出来。![3789F9F0](C:\Users\wangw\AppData\Local\Temp\SGPicFaceTpBq\9960\3789F9F0.png)，还有两周就要直面天命了
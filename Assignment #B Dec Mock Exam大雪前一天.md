# Assignment #B: Dec Mock Exam大雪前一天



Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）⽉考： AC1（请改为同学的通过数） 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### E22548: 机智的股民老张



http://cs101.openjudge.cn/practice/22548/

思路：

代码：

```
a=list(map(int,input().split()))
n=len(a)
k=[]
d=[(i,a[i]) for i in range(n)]
d.sort(key=lambda x:x[1] )
for i in range(n):
    for j in range(n-i-2):
        if d[i][0]<d[n-j-1][0]:
            c=d[n-j-1][1]-d[i][1]
            k.append(c)
            break
print(max(k))
```

![image-20241210213050426](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241210213050426.png)

### M28701: 炸鸡排



greedy, http://cs101.openjudge.cn/practice/28701/

思路：看了解答，没想到能写这么短

代码：

```
n, k = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
s = sum(t)
while True:
    if t[-1] > s / k:
        s -= t.pop()
        k -= 1
    else:
        print(f'{s / k:.3f}')
        break
```



![image-20241210222342027](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241210222342027.png)

### M20744: 土豪购物



dp, http://cs101.openjudge.cn/practice/20744/

思路：

代码：

```
a = list(map(int, input().split(',')))
dp1 = [0] * len(a);
dp2 = [0] * len(a)
dp1[0] = a[0];
dp2[0] = a[0]
for i in range(1, len(a)):
    dp1[i] = max(dp1[i - 1] + a[i], a[i])
    dp2[i] = max(dp1[i - 1], dp2[i - 1] + a[i], a[i])
print(max(dp2))
```



![image-20241210222532311](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241210222532311.png)

### T25561: 2022决战双十一



brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

代码：

```
result = float("inf")
n, m = map(int, input().split())
store_prices = [input().split() for _ in range(n)]
coupons = [input().split() for _ in range(m)]

def dfs(store_prices, coupons, items=0, total_price=0, each_store_price=[0] * m):
    global result
    if items == n:
        # 查看店铺券使用情况
        coupon_price = 0
        for i in range(m):
            # 在这个店铺可以减的金额
            #store_p = max([int(coupon.split('-')[1]) for coupon in store_coupon if each_store_price[i] >= int(coupon.split('-')[0])], default=0)           
            store_p = 0
            for coupon in coupons[i]:
                a, b = map(int, coupon.split('-'))
                if each_store_price[i] >= a:
                    store_p = max(store_p, b)
            
            coupon_price += store_p

        result = min(result, total_price - (total_price // 300) * 50 - coupon_price)
        return

    for i in store_prices[items]:
        idx, p = map(int, i.split(':'))
        each_store_price[idx - 1] += p
        dfs(store_prices, coupons, items + 1, total_price + p, each_store_price)
        each_store_price[idx - 1] -= p


dfs(store_prices, coupons)
print(result)
```



![image-20241210222710699](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241210222710699.png)

### T20741: 两座孤岛最短距离



dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

代码：

```
from collections import deque

# 输入和初始化
n = int(input())
landkarte = [list(map(int, input())) for _ in range(n)]

# 方向向量
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 标记岛屿并返回第一个岛屿的边界点
def mark_islands():
    visited = [[False] * n for _ in range(n)]
    island1_boundary = []
    queue = deque()

    # 找到第一个岛屿，使用DFS标记，并记录边界点
    def dfs(x, y):
        visited[x][y] = True
        queue.append((x, y))
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if landkarte[nx][ny] == 1:
                        dfs(nx, ny)
                    else:
                        # 当前是边界点
                        island1_boundary.append((x, y))

    # 开始寻找第一个岛屿
    for i in range(n):
        for j in range(n):
            if landkarte[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                # 此时已经标记完第一个岛屿
                return visited, island1_boundary

# 多源BFS寻找最短路径
def shortest_bridge():
    visited, island1_boundary = mark_islands()
    queue = deque(island1_boundary)
    steps = 0

    # 多源BFS扩展
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if landkarte[nx][ny] == 1:
                            # 遇到另一个岛屿
                            return steps
                        queue.append((nx, ny))
        steps += 1

# 输出最短路径
print(shortest_bridge())
```



![image-20241210220904967](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241210220904967.png)

### T28776: 国王游戏



greedy, http://cs101.openjudge.cn/practice/28776

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

## 2. 学习总结和收获



这次月考太难了，后面的题题干又长，根本没时间读，
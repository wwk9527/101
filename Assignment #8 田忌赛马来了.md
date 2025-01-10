# Assignment #8: 田忌赛马来了



Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### 12558: 岛屿周⻓



matices, http://cs101.openjudge.cn/practice/12558/

思路：

代码：

```
def island_perimeter(grid):
    n = len(grid)
    m = len(grid[0])
    perimeter = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # 每个陆地格子默认贡献4个边
                perimeter += 4
                
                # 检查上方是否有相邻陆地
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # 上方和下方各减1个边
                
                # 检查左方是否有相邻陆地
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # 左方和右方各减1个边
    
    return perimeter

# 读取输入
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 计算并输出结果
print(island_perimeter(grid))
```



![image-20241112194634345](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241112194634345.png)

### LeetCode54.螺旋矩阵



matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

代码：

```
def generate_spiral_matrix(n):
    # 创建一个n*n的矩阵，初始值为0
    matrix = [[0] * n for _ in range(n)]
    
    # 定义方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 当前方向的索引
    
    # 起始位置
    row, col = 0, 0
    
    # 填充矩阵
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
        
        # 检查下一个位置是否超出边界或已被填充
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            direction_index = (direction_index + 1) % 4  # 改变方向
        
        # 更新当前位置
        row += directions[direction_index][0]
        col += directions[direction_index][1]
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# 主程序
if __name__ == "__main__":
    n = int(input())  # 读取输入
    spiral_matrix = generate_spiral_matrix(n)  # 生成螺旋矩阵
    print_matrix(spiral_matrix)  # 打印矩阵
```



![image-20241112182908012](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241112182908012.png)

### 04133:垃圾炸弹



matrices, http://cs101.openjudge.cn/practice/04133/

思路：

代码：

```
def max_trash_cleaned(d, points):
    # 初始化最大垃圾量和对应的投放点数目
    max_trash = 0
    best_count = 0
    
    # 遍历所有可能的投放点
    for x in range(1025):
        for y in range(1025):
            # 计算当前投放点能够清除的垃圾总量
            trash_sum = 0
            for px, py, pi in points:
                if abs(px - x) <= d and abs(py - y) <= d:
                    trash_sum += pi
            
            # 更新最大垃圾量和对应的投放点数目
            if trash_sum > max_trash:
                max_trash = trash_sum
                best_count = 1
            elif trash_sum == max_trash:
                best_count += 1
    
    return best_count, max_trash

# 读取输入
d = int(input())
n = int(input())
points = []
for _ in range(n):
    x, y, i = map(int, input().split())
    points.append((x, y, i))

# 计算并输出结果
best_count, max_trash = max_trash_cleaned(d, points)
print(best_count, max_trash)
```



![image-20241112185659522](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241112185659522.png)

### LeetCode376.摆动序列



greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

代码：

```
def wiggleMaxLength(nums):
    n = len(nums)
    if n < 2:
        return n
    
    # 初始化状态
    up = [1] * n
    down = [1] * n
    
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]
    
    return max(up[n - 1], down[n - 1])

# 读取输入
n = int(input())
nums = list(map(int, input().split()))

# 计算并输出结果
print(wiggleMaxLength(nums))
```

![image-20241112200758632](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241112200758632.png)

### CF455A: Boredom



dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

代码：

```
from collections import defaultdict

def max_points(nums):
    # 统计每个数字出现的次数
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    
    # 找到最大值
    max_num = max(count.keys())
    
    # 初始化 dp 数组
    dp = [0] * (max_num + 1)
    
    # 填充 dp 数组
    for i in range(1, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    return dp[max_num]

# 输入处理
n = int(input())
nums = list(map(int, input().split()))

# 输出结果
print(max_points(nums))
```



![image-20241116125642044](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241116125642044.png)

### 02287: Tian Ji -- The Horse Racing



greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

## 2. 学习总结和收获

用dp很简单，但思路很难想到，我还在找感觉。

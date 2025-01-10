# Assignment #A: dp & bfs



Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### LuoguP1255 数楼梯



dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

代码：

```
N=int(input())
d=[0]*N
i=1
while i<=N:
    if i==1:
        d[i-1]=1
    elif i==2:
        d[i-1]=2
    else:
        d[i-1]=d[i-2]+d[i-3]
    i+=1
print(d[N-1])
```



![image-20241128213147574](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241128213147574.png)

### 27528: 跳台阶



dp, http://cs101.openjudge.cn/practice/27528/

思路：

代码：

```
N = int(input())
d=[0]*N
i=0
while i<N:
    if i==0:
        d[i]=1
    elif i==1:
        d[i]=2
    else:
        for j in range(i):
            d[i]+=d[j]
        d[i]+=1
    i+=1
print(d[N-1])
```



![image-20241128213858853](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241128213858853.png)

### 474D. Flowers



dp, https://codeforces.com/problemset/problem/474/D

思路：

代码：

```
MOD = 10**9 + 7

def precompute(k):
    max_flowers = 10**5
    dp = [0] * (max_flowers + 1)
    dp[0] = 1  # 没有花的情况
    
    # 动态规划填充 dp 数组
    for i in range(1, max_flowers + 1):
        dp[i] = dp[i - 1]  # 加一个红花
        if i >= k:
            dp[i] = (dp[i] + dp[i - k]) % MOD  # 加 k 个白花
    
    # 计算前缀和数组
    prefix_sum = [0] * (max_flowers + 2)  # 多加一位方便处理边界情况
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = (prefix_sum[i - 1] + dp[i - 1]) % MOD
    
    return prefix_sum

# 读取输入
t, k = map(int, input().split())
cases = [tuple(map(int, input().split())) for _ in range(t)]

# 预计算
prefix_sum = precompute(k)

# 解决问题并输出答案
for a, b in cases:
    result = (prefix_sum[b + 1] - prefix_sum[a]) % MOD
    print(result)
```



![image-20241130004404815](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241130004404815.png)

### LeetCode5.最长回文子串



dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

代码：

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 辅助函数：从中心扩展找到最长回文子串长度
        def expand_around_center(s: str, left: int, right: int) -> int:
            L, R = left, right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        if not s:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_around_center(s, i, i)  # 奇数长度的回文
            len2 = expand_around_center(s, i, i + 1)  # 偶数长度的回文
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

# 示例
s1 = "babad"
s2 = "cbbd"

solution = Solution()
print(solution.longestPalindrome(s1))  # 输出 "bab" 或 "aba"
print(solution.longestPalindrome(s2))  # 输出 "bb"
```



![image-20241129122011148](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241129122011148.png)

### 12029: 水淹七军



bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

### 02802: 小游戏



bfs, http://cs101.openjudge.cn/practice/02802/

思路：

代码：

```

```



代码运行截图 （至少包含有"Accepted"）

## 2. 学习总结和收获



最后两道题太难了，不会做，前两道题很简单，现在在写力扣，发现力扣的解答视频非常好，易理解。
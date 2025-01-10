'''a=input()
nums=[int(x) for x in a[a.index('['):a.index(']')+1] if x.isdigit()]
k1=[x for x in a[a.index('k'):] if x.isdigit()]
k=int(''.join(k1))'''
from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []

    result = []
    window = deque()

    for i in range(len(nums)):
        # 移除不在当前窗口范围内的元素
        if window and window[0] <= i - k:
            window.popleft()

        # 移除所有小于当前元素的索引，因为它们不可能成为窗口的最大值
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # 添加当前元素的索引到队列
        window.append(i)

        # 当窗口大小达到 k 时，开始记录结果
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# 读取输入
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 计算并打印结果
dp = maxSlidingWindow(nums, k)
print(' '.join(str(x) for x in dp))
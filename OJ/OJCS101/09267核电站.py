def count_safe_placements(N, M):
    # 初始化DP表，额外增加一行用于处理边界情况
    dp = [[0 for _ in range(M)] for _ in range(N + 1)]
    dp[0][0] = 1  # 没有坑的情况下，只有一种情况，即什么也不做
    for i in range(1, N + 1):
        # 第 i 个坑不放核物质的情况
        dp[i][0] = sum(dp[i - 1])

        # 第 i 个坑放核物质的情况
        for j in range(1, M):
            if i - 1 >= 0:
                dp[i][j] = dp[i - 1][j - 1]
    # 计算最终结果
    result = sum(dp[N])
    return result
# 示例用法
N, M = map(int, input().split())
print(count_safe_placements(N, M))




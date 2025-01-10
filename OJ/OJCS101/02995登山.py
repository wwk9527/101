def longest_mountain_path(N, altitudes):
    # 计算最长上升子序列长度
    up = [1] * N
    for i in range(1, N):
        for j in range(i):
            if altitudes[j] < altitudes[i] and altitudes[j] != altitudes[i]:
                up[i] = max(up[i], up[j] + 1)

    # 计算最长非上升子序列长度
    down = [1] * N
    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            if altitudes[j] <= altitudes[i] and altitudes[j] != altitudes[i]:
                down[i] = max(down[i], down[j] + 1)

    # 结果计算
    result = 0
    for i in range(N):
        if up[i] > 1 and down[i] > 1:  # 确保有上升和下降部分
            result = max(result, up[i] + down[i] - 1)

    return result if result > 0 else 1  # 如果没有符合条件的路径，至少可以游览一个景点

# 测试用例
n=int(input())
sit=list(map(int,input().split()))
print(longest_mountain_path(n,sit))  # 输出应为 4
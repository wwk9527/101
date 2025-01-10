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
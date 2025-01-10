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


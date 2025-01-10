# 数院胡睿诚
# 1）按照区间左端点从小到大排序。
# 2）从前往后依次枚举每个区间，在所有能覆盖当前目标区间起始位置start的区间之中，
#   选择右端点最大的区间。
#   假设右端点最大的区间是第 i 个区间，右端点为 ri；
#   最后将目标区间的start更新成 ri + 1。

def calculate_min_coverage(n, points):
    clips = [(max(0, i-point), min(n-1, i+point))
             for i, point in enumerate(points)]
    clips.sort()

    st, ed = 0, n-1
    res = 0

    current_index = 0
    while current_index < n:
        maxR = -float("inf")
        while current_index < n and clips[current_index][0] <= st:
            maxR = max(maxR, clips[current_index][1])
            current_index += 1
        if maxR < st:
            break
        res += 1
        if maxR >= ed:
            break
        st = maxR + 1
    return res

N = int(input())
points = list(map(int, input().split()))
print(calculate_min_coverage(N, points))
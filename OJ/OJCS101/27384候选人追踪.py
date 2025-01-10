n, k = map(int, input().split())
a = list(map(int, input().split()))
s = set(map(int, input().split()))  # 使用集合 s 来提高查找效率

# 构建 lis 列表，每个元素是一个 (time, value) 元组
lis = [(a[i], a[i + 1]) for i in range(0, 2 * n, 2)]

# 初始化 sat 和 other 字典
sat = {val: 0 for val in s}
other = {}

# 排序 lis 列表
lis.sort()

# 初始化时间点集合 tim
tim = set()
current_sat_count = 0
current_other_count = 0

for x in range(n):
    time, value = lis[x]

    if value in sat:
        sat[value] += 1
        current_sat_count += 1
    else:
        if value not in other:
            other[value] = 0
        other[value] += 1
        current_other_count += 1

    # 检查当前是否满足条件
    if min(sat.values(), default=0) > max(other.values(), default=0):
        tim.add(time)

# 输出结果
ans = len(tim)
if ans > 0 and max(tim) == lis[-1][0]:
    print(ans - 1)
else:
    print(ans)


    



n = int(input())
a = list(map(int, input().split()))
b = list(range(1, n + 1))

# 使用 sorted 来对 (时间, 编号) 进行排序
c = sorted(zip(a, b))

s = [time for time, index in c]  # 对应的时间列表
f = [index for time, index in c]  # 对应的实验编号列表

x = 0
for i in range(len(f)):
    x += s[i] * (n-i-1)

print(*f)
print(f'{x / len(f):.2f}')  # 注意这里是用 len(f) 来计算均值


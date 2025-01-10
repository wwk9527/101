'''n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
if n==1:
    print(m[0][0])
else:
    if n % 2 == 0:
        s = []
        for i in range(n // 2):
            r1 = sum(m[i][j] for j in range(i, n - i))
            r2 = sum(m[n - 1 - i][j] for j in range(i, n - i))
            c1 = sum(m[j][i] for j in range(i, n - i))
            c2 = sum(m[j][n - 1 - i] for j in range(i, n - i))
            s.append(r1 + r2 + c1 + c2 - m[i][i] - m[n - 1 - i][n - 1 - i] - m[i][n - 1 - i] - m[n - 1 - i][i])
        print(max(s))
    else:
        s = [m[(n - 1) // 2][(n - 1) // 2]]
        for i in range((n - 1) // 2):
            r1 = sum(m[i][j] for j in range(i, n - i))
            r2 = sum(m[n - 1 - i][j] for j in range(i, n - i))
            c1 = sum(m[j][i] for j in range(i, n - i))
            c2 = sum(m[j][n - 1 - i] for j in range(i, n - i))
            s.append(r1 + r2 + c1 + c2 - m[i][i] - m[n - 1 - i][n - 1 - i] - m[i][n - 1 - i] - m[n - 1 - i][i])
        print(max(s))
'''


def max_layer_sum(matrix):
    n = len(matrix)
    max_sum = 0

    # 定义四个方向上的边界
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        current_sum = 0

        # 上边一行
        for i in range(left, right + 1):
            current_sum += matrix[top][i]
        top += 1

        # 右边一列
        for i in range(top, bottom + 1):
            current_sum += matrix[i][right]
        right -= 1

        if top <= bottom:
            # 下边一行
            for i in range(right, left - 1, -1):
                current_sum += matrix[bottom][i]
            bottom -= 1

        if left <= right:
            # 左边一列
            for i in range(bottom, top - 1, -1):
                current_sum += matrix[i][left]
            left += 1

        # 更新最大层的和
        max_sum = max(max_sum, current_sum)

    return max_sum


# 读取输入
n = int(input().strip())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# 调用函数并输出结果
print(max_layer_sum(matrix))

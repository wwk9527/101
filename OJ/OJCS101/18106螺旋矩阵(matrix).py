def generate_spiral_matrix(n):
    # 创建一个n*n的矩阵，初始值为0
    matrix = [[0] * n for _ in range(n)]

    # 定义方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 当前方向的索引

    # 起始位置
    row, col = 0, 0

    # 填充矩阵
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        # 检查下一个位置是否超出边界或已被填充
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            direction_index = (direction_index + 1) % 4  # 改变方向

        # 更新当前位置
        row += directions[direction_index][0]
        col += directions[direction_index][1]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


# 主程序
if __name__ == "__main__":
    n = int(input())  # 读取输入
    spiral_matrix = generate_spiral_matrix(n)  # 生成螺旋矩阵
    print_matrix(spiral_matrix)  # 打印矩阵
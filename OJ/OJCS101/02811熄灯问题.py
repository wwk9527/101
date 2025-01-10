def press_button(grid, row, col):
    for r, c in [(row, col), (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < 5 and 0 <= c < 6:
            grid[r][c] = 1 - grid[r][c]


def solve_lights_out(initial_state):
    # 尝试所有第一行按钮的组合（2^6种）
    for first_row_mask in range(64):  # 从0到63，表示第一行的所有可能组合
        # 复制初始状态并转换为可变列表
        grid = [list(row) for row in initial_state]
        solution = [[0] * 6 for _ in range(5)]

        # 应用第一行的按钮组合
        for col in range(6):
            if first_row_mask & (1 << col):
                press_button(grid, 0, col)
                solution[0][col] = 1

        # 根据第一行的结果处理剩余行
        for row in range(1, 5):
            for col in range(6):
                if grid[row - 1][col] == 1:  # 如果上一行的灯是亮的
                    press_button(grid, row, col)
                    solution[row][col] = 1

        # 检查最后一行是否全灭
        if all(cell == 0 for cell in grid[-1]):
            return solution

    # 如果没有找到解，则返回None
    return None


# 输入读取
import sys

input_data = sys.stdin.read().strip()
lines = input_data.split('\n')
initial_state = [list(map(int, line.split())) for line in lines]

# 解决问题并输出答案
solution = solve_lights_out(initial_state)
if solution is not None:
    for row in solution:
        print(" ".join(str(x) for x in row))
else:
    print("No solution found")


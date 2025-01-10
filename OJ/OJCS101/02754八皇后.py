from itertools import permutations
def is_valid(board):
    """
    检查给定的皇后串是否有效。
    参数:
    board (tuple): 一个长度为8的元组，表示一种可能的皇后放置方案
    返回:
    bool: 如果该方案有效，则返回True；否则返回False
    """
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True
def generate_solutions():
    """
    生成所有有效的八皇后解，并按字典序排序。
    返回:
    list: 包含所有有效解的列表，每个解是一个长度为8的字符串
    """
    solutions = []
    # 生成所有可能的列排列（0-7）
    for perm in permutations(range(8)):
        if is_valid(perm):
            solutions.append(''.join(str(x + 1) for x in perm))
    solutions.sort()  # 按字典序排序
    return solutions
# 预先计算并存储所有解
solutions = generate_solutions()
# 主程序开始
n = int(input())  # 获取测试数据的组数
results = []
for _ in range(n):
    b = int(input())  # 获取每组测试数据中的索引b
    results.append(solutions[b - 1])  # 注意：用户输入的b是从1开始的，所以需要减1
# 输出结果
for result in results:
    print(result)
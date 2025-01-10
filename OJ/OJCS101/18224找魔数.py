import math

def can_be_sum_of_squares(x):
    # 检查 x 是否能表示为两个平方数之和
    for i in range(1, int(math.sqrt(x)) ):
        if math.floor((x-i**2)**0.5) == (x-i**2)**0.5 :
            return True
    return False

m = int(input())
xi = list(map(int, input().split()))

for i in xi:
    if can_be_sum_of_squares(i):
        print(f'{bin(i)} {oct(i)} {hex(i).lower()}')
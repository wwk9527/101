import math

x=4.5
T = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        v_t = []
        for i in range(n):
            v, t = map(int, input().split())
            if t >= 0:
                v_t.append(math.ceil(x * 3600 / v + t))
            else:
                continue
        T.append(min(v_t))
print(*T, sep='\n')

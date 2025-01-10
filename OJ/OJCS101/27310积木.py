def dfs(x, used_cubes):
    if x == len(word):
        return True
    current_char = word[x]
    if current_char in ans:
        for cube_index in ans[current_char]:
            if cube_index not in used_cubes:
                used_cubes.add(cube_index)
                if dfs(x + 1, used_cubes):
                    return True
                used_cubes.remove(cube_index)  # 回溯
    return False


n = int(input())
cubes = []
for _ in range(4):
    cubes.append(set(input().strip()))

for _ in range(n):
    word = input().strip()
    ans = {}

    # 构建字典，记录每个字符可以在哪些积木上找到
    for i, cube in enumerate(cubes):
        for char in cube:
            if char not in ans:
                ans[char] = [i]
            else:
                ans[char].append(i)

    # 预处理检查
    if len(word) > 4 or any(word.count(char) > sum(char in cube for cube in cubes) for char in set(word)):
        print("NO")
        continue

    if dfs(0, set()):
        print("YES")
    else:
        print("NO")















n=int(input())
ans=0
for i in range(((3*n)//5)*5,0,-5):
    if ans>0:
        break
    for k in range(n, 0, -1):
        if ans > 0:
            break
        for j in range(n, 0, -1):
            if ans > 0:
                break
            if i - k - j >n:
                break
            if (i - k) % 2 == 0 and (i - j) % 3 == 0:
                ans += i
            elif (i - j) % 2 == 0 and (i - k) % 3 == 0:
                ans += i
            elif (k + j) % 2 == 0 and (i - k) % 3 == 0:
                ans += i
            elif (k + j) % 3 == 0 and (i - k) % 2 == 0:
                ans += i
            elif (k + j) % 2 == 0 and (i - j) % 3 == 0:
                ans += i
            elif (k + j) % 3 == 0 and (i - j) % 2 == 0:
                ans += i
print(ans)

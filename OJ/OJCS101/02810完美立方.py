import math
n=int(input())
ans=[]
for i in range(1,n+1):
    for j in range(2,i):
        for k in range(2,j+1):
            for l in range(2,k+1):
                if i**3==j**3+k**3+l**3:
                    ans.append((i,l,k,j))
ans.sort()
for i in ans:
    print(f'Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})')
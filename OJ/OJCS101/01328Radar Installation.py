from math import sqrt
id=1
while True:
    n,d = map(int,input().split())
    if n==0 and d==0:
        break
    xy=[tuple( map(int,input().split())) for j in range(n)]
    sorted_xy=sorted(xy,key=lambda x:x[0])
    if d<max(sorted_xy,key=lambda x:x[1])[1]:
        print(f"Case {id}: -1")
        id += 1
        input()
        continue
    ran=[]
    for i in range(n):
        if sorted_xy[i][1]==d:
            ran.append((sorted_xy[i][0],sorted_xy[i][0]))
        else:
            left=sorted_xy[i][0]-sqrt(d**2-sorted_xy[i][1]**2)
            right=sorted_xy[i][0]+sqrt(d**2-sorted_xy[i][1]**2)
            ran.append((left,right))
    ran.sort(key=lambda x:x[0])
    z=1
    for i in range(len(ran)-1):
        if ran[i][1]>=ran[i+1][0]:
            if ran[i][1]<=ran[i+1][0]:
                ran[i+1]=(ran[i+1][0],ran[i][1])
            else:
                ran[i+1]=(ran[i+1][0],ran[i+1][1])
            continue
        z+=1
    print(f"Case {id}: {z}")
    id+=1
    input()



def s1(board,x1,y1,x2,y2,m):
    a


while True:
    w,h=map(int,input().split())
    n=1
    if w==0 and h==0:
        break
    board=[]
    board.append([0]*(w+2))
    for i in range(w):
        a=input()
        ro=[]
        ro.append(0)
        for j in range(len(a)):
            if a[j]=='X':
                ro.append(1)
            else:
                ro.append(0)
        ro.append(0)
        board.append(ro)
    board.append([0]*(w+2))
    print("Board #"+str(n)+":")
    while True:
        m=1
        x1,y1,x2,y2=map(int,input().split())
        if x1==0 and y1==0 and x2==0 and y2==0:
            break
        s1(board,x1,y1,x2,y2,m)




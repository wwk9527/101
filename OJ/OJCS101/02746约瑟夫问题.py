while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    an=list(range(1,n+1))
    i=1
    j=1
    while len(an)>1:
        if i ==m:
            an.pop(j-1)
            i=1
            j-=1
        else:
            i+=1
        if j==len(an):
            j=1
        else:
            j+=1
    print(an[0])
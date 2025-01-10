t=int(input())
for i in range(t):
    l,n=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    mi=[]
    ma=[]
    for i in range(n):
        mi.append(min(li[i],l- li[i]))
        ma.append(max(li[i],l- li[i]))
    print(max(mi),max(ma))



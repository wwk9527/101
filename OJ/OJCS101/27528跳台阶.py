N = int(input())
d=[0]*N
i=0
while i<N:
    if i==0:
        d[i]=1
    elif i==1:
        d[i]=2
    else:
        for j in range(i):
            d[i]+=d[j]
        d[i]+=1
    i+=1
print(d[N-1])
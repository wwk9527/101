def isa(d,a):
    max=0
    bes=0
    for x in range(1025):
        for y in range(1025):
            sum=0
            for t,z,i in s:
                if t in range(x-d,x+d+1) and z in range(y-d,y+d+1):
                    sum+=i
            if sum>=bes:
                bes=sum
                max=+1
    return f'{max} {bes}'



d=int(input())
n=int(input())
s=[]
for i in range(n):
    x,y,i=tuple(map(int,input().split()))
    s.append((x,y,i))
s.sort(key=lambda x:(x[0],x[1]))
print(isa(d,s))



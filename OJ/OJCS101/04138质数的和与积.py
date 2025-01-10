def pan(i):
    a=[]
    for j in range(1,i):
        if i%j==0:
            a.append(j)
    if len(a)==1:
        return True
    else:
        return False
s=int(input())
t=s//2
for i in range(t,-1,-1):
    if pan(i) and pan(s-i):
        ans=i*(s-i)
        print(ans)
        break
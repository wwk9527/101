L,M=map(int,input().split())
L_=set(range(0,L+1))
a_b = set()
for i in range(M):
    a,b=map(int,input().split())
    a_b.update(set(range(a,b+1)))
x=len(L_-a_b)
print(x)
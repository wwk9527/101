from math import log
t=int(input())
for i in range(t):
    a=int(input())
    ans=((1+a)*a)//2
    for i in range(a):
        if 2**i<=a and 2**(i+1)>a:
            ans-=2*(2**(i+1)-1)
            break
    print(ans)



H,l,n=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
v0=v[(n-1)//2]
t0=l/v0
h=H-0.5*10*t0**2
print(f'{h:.2f}')
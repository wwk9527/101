a=int(input())
mi=0
ma=0
for i in range(0,a+1):
    if (a-2*i)%4==0:
        mi=i+(a-2*i)//4
        break
for i in range(0,a+1):
    if (a-4*i)%2==0:
        ma=i+(a-4*i)//2
        break
print(mi,ma)
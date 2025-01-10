x=int(input())
if x>=6 and x%2==0:
    for i in range(3,x//2+1):
        a=[]
        if i%2!=0:
            for j in range(2,i+1):
                if i %j==0:
                    a.append(j)
        if (x-i)%2!=0:
            for j in range(2,x-i+1):
                if (x-i) %j==0:
                    a.append(j)
        if len(a)==2:
            print(f'{x}={i}+{x-i}')
else:
    print('Error!')
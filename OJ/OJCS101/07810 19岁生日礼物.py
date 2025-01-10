n=int(input())
for i in range(n):
    p=int(input())
    if p%19==0:
        print("Yes")
    elif str(p).count("19")>=1:
        print("Yes")
    else:
        print("No")
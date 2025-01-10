n=int(input())
a=bin(n)[2:]
if a[::-1]==a:
    print('Yes')
else:
    print('No')
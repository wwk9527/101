import random
l=[]
n,d=map(int,input().split())
'''for i in range(n) :
    l.append(random.randint(1,10))'''
a=[]
for i in range(n):
    a.append(int(input()))
b=sorted(a ,reverse=True)
for i in range(n):

print(*a,sep='\n')


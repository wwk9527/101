n,m1,m2=map(int,input().split())
a1=[list(map(int,input().split())) for i in range(m1)]
a2=[list(map(int,input().split())) for i in range(m2)]
z={}
b2=[i[1] for i in a2]
for i in a1:
    for j in a2:
        if i[1]==j[0]:
            if (i[0],j[1]) not in z.keys():
                z[(i[0],j[1])]=i[2]*j[2]
            else:
                z[(i[0],j[1])]+=i[2]*j[2]
ans=[]
for i in z.keys():
    ans.append((*i,z[i]))
ans.sort()
for i in ans:
    print(i[0],i[1],i[2])
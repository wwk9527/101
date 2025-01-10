an=list(map(int,input().split()))
an.sort()
n=len(an)
i=0
ans=set()
while i<n-2:
    j=i+1
    k=n-1
    while j<k:
        if an[i]+an[j]+an[k]>0:
            k-=1
        elif an[i]+an[j]+an[k]<0:
            j+=1
        else:
            ans.add((an[i],an[j],an[k]))
            if j==k-1:
                break
            else:
                if an[j+1]==an[j]:
                    j+=1
                elif an[k-1]==an[k]:
                    k-=1
                else:
                    j+=1
    i+=1
print(len(ans))











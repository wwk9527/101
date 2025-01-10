a=input()
ans=[]
n=0
for i in range(len(a)):
    if a[i]=='^':
        n+=1
        a0=[]
        b0=[]
        for j in range(i-2,-1,-1):
            if a[j]=='+' :
                break
            a0.append(a[j])
        for j in range(i+1,len(a),1):
            if a[j]=='+':
                break
            b0.append(a[j])
        a1=''.join(a0[::-1])
        b1=''.join(b0)
        if  len(a1)==0:
            ans.append(int(b1))
        elif int(a1)!=0:
            ans.append(int(b1))

if n==0:
    print('n^0')
else:
    k=max(ans)
    print(f'n^{k}')



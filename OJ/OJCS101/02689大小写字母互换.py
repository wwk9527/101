ans=input()
ans1=[]
for i in ans:
    if i.isalpha():
        if i.upper()==i:
            ans1.append(i.lower())
        else:
            ans1.append(i.upper())
    else:
        ans1.append(i)
print(''.join(str(i) for i in ans1))
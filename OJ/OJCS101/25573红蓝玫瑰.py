r=list(input())
n=len(r)
R=[0]*n
B=[0]*n
if r[0]=="R":R[0]=0;B[0]=1
else:R[0]=1;B[0]=0
for i in range(n-1):
    if r[i+1]=="R":
        R[i+1]=R[i]
        B[i+1]=min(R[i],B[i])+1
    else:
        R[i+1]=min(R[i],B[i])+1
        B[i+1]=B[i]
print(R[-1])
'''def blu(blue):
    n = len(blue)
    duan = []
    for i in range(1, n):
        if blue[i] - blue[i-1] != 1:
            duan.append(i)
    if len(duan) == 0:
        if blue[0] == 0:
            return 1
        else:
            return 2
    else:
        yiduan = []
        for i in range(len(duan)):
            if i == 0:
                yiduan.append(blue[:duan[i]])
            if i == len(duan) - 1:
                yiduan.append(blue[duan[i]:])
            if i != 0 and i != len(duan) - 1:
                yiduan.append(blue[duan[i]:duan[i + 1]])
        ans = 0
        for i in yiduan:
            if i[0] == 0:
                ans += 1
            else:
                if len(i) == 1:
                    ans += 1
                else:
                    ans += 2
        return ans
str=input()
n=len(str)
dp=[0]*n
blue=[]
red=[]
for i in range(n):
    if str[i] =='B':
        blue.append(i)
    elif str[i] =='R':
        red.append(i)
nb=len(blue)
nr=len(red)
if nb==0 :
    print(0)
elif nb==1 or nr==0:
    print(1)
elif nr==1:
    print(2)
else:
    ans=min(blu(blue),blu(red)+1)
    print(ans)'''












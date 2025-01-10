# Assignment #7: Nov Mock Exam立冬



Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by 同学的姓名、院系

**说明：**

1）⽉考： AC**2**（请改为同学的通过数） 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora [https://typoraio.cn](https://typoraio.cn/) ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目



### E07618: 病人排队



sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

代码：

```
n=int(input())
id=[]
for i in range(n):
    x,y=input().split()
    id.append((x,int(y)))
old=[]
you=[]
for x in id:
    if x[1]>=60:
        old.append(x)
    else:
        you.append(x)
if len(old)==0:
    for x in id:
        print(x[0])
elif len(you)==0:
    old.sort(key=lambda x: x[1],reverse=True)
    for x in old:
        print(x[0])
else:
    old.sort(key=lambda x: x[1],reverse=True)
    for x in old:
        print(x[0])
    for x in you:
        print(x[0])


```

![image-20241110132445252](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110132445252.png)

### E23555: 节省存储的矩阵乘法



implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

代码：

```
n,m1,m2=map(int,input().split())
X0=[]
Y0=[]
for i in range(m1):
    x=tuple(map(int,input().split()))
    X0.append(x)
for i in range(m2):
    x=tuple(map(int,input().split()))
    Y0.append(x)

X=[[0]*n for i in range(n)]
Y=[[0]*n for i in range(n)]
for i in X0:
    x=i[0]
    y=i[1]
    X[x][y]+=i[2]
for i in Y0:
    x=i[0]
    y=i[1]
    Y[x][y]+=i[2]
Z=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        Z[i][j]=sum(X[i][k]*Y[k][j] for k in range(n))
for i in range(len(Z)):
    for j in range(len(Z[i])):
        if Z[i][j]!=0:
            print(f'{i} {j} {Z[i][j]}')
```

![image-20241110132521478](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110132521478.png)

### M18182: 打怪兽



implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

代码：

```
nc = int(input())

for _ in range(nc):
    n, m, b = map(int, input().split())
    skills = []

    for j in range(n):
        ti, xi = map(int, input().split())
        skills.append((ti, xi))
    skills.sort(key=lambda x: (x[0],-x[1]))
    skills.append((0,0))
    sk={}
    a=[]
    for i in range(n):
        if skills[i][0]==skills[i+1][0] :
            a.append(skills[i][1])
        else:
            a.append(skills[i][1])
            sk.update({skills[i][0]:a})
            a=[]
    for x in sk:
        b-=sum(i for i in sk[x][:min(len(sk[x]),m)])
        if b<=0:
            print(x)
            break
    if b>0:
        print('alive')
```



![image-20241110194644940](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110194644940.png)

### M28780: 零钱兑换3



dp, http://cs101.openjudge.cn/practice/28780/

思路：

代码：

```
n, m = map(int, input().split())
va = list(map(int, input().split()))
va.sort(reverse=True)

# 初始化 dp 数组，dp[i] 表示达到 i 所需的最少步数
dp = [float('inf')] * (m + 1)
dp[0] = 0  # 初始状态，达到 0 所需的步数为 0

for value in va:
    for j in range(value, m + 1):
        dp[j] = min(dp[j], dp[j - value] + 1)

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])
```



![image-20241110171018198](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110171018198.png)

### T12757: 阿尔法星人翻译官



implementation, http://cs101.openjudge.cn/practice/12757

思路：先检验百万，再千，最后归到百的数字好计算，虽然答案有81行，但是都有重叠代码，直接复制粘贴了。

代码：

```
def solution(result):
    if sum(result) < 100:
        return sum(result)
    else:
        if sum(result) > 1000000:
            a = result.index(1000000)
            b = result[:a + 1]
            c = result[a + 1:]
            x1 = 0
            for i in b:
                if i < 100:
                    x1 += i
                else:
                    x1 *= i
            x2 = 0
            if sum(c) >= 1000:
                d = c.index(1000)
                e = c[:d + 1]
                f = c[d + 1:]
                for i in e:
                    if i < 100:
                        x2 += i
                    else:
                        x2 *= i
                x3 = 0
                for i in f:
                    if i < 100:
                        x3 += i
                    else:
                        x3 *= i
                return (x1 + x2 + x3)
            else:
                for i in c:
                    if i < 100:
                        x2 += i
                    else:
                        x2 *= i
                return (x1 + x2)
        elif 1000<sum(result)<1000000 :
            a = result.index(1000)
            b = result[:a + 1]
            c = result[a + 1:]
            x1 = 0
            for i in b:
                if i < 100:
                    x1 += i
                else:
                    x1 *= i
            x2 = 0
            for i in c:
                if i < 100:
                    x2 += i
                else:
                    x2 *= i
            return (x1 + x2)
        else:
            x2 = 0
            for i in result:
                if i < 100:
                    x2 += i
                else:
                    x2 *= i
            return x2
a='negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million'
a=a.split(', ')
b=list(a)
c=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000,1000000]
d=dict(zip(b,c))
string=input()
string=string.split()
al=[]
for i in string:
    al.append(d[i])
if len(al)==1:
    print(al[0])
else:
    if -1 in al:
        al.remove(-1)
        print(-1*solution(al))
    else:
        print(solution(al))
```



![image-20241110190603259](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110190603259.png)

### T16528: 充实的寒假生活



greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

代码：

```
def max_activities(n, activities):
    # 按结束时间排序
    activities.sort(key=lambda x: x[1])
    
    # 选择第一个活动
    last_end_time = -1
    count = 0
    
    for start, end in activities:
        if start > last_end_time:  # 注意这里使用 '>' 而不是 '>='
            count += 1
            last_end_time = end
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    activities = []
    for _ in range(n):
        start = int(data[index])
        end = int(data[index + 1])
        activities.append((start, end))
        index += 2
    
    result = max_activities(n, activities)
    print(result)

if __name__ == "__main__":
    main()
```

![image-20241110200956465](C:\Users\wangw\AppData\Roaming\Typora\typora-user-images\image-20241110200956465.png)

## 2. 学习总结和收获



月考只AC两个，都有思路，但是每道题都用用时较长:40分钟左右.期中复习有点紧，最近都没做计概题，需要发力了。
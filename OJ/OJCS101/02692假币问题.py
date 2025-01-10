n = int(input())
for case in range(1, n + 1):
    heav=[]
    ligh=[]
    al=set()
    for i in range(3):
        a = input().split()
        x1 = list(a[0])
        x2 = list(a[1])
        x3 = a[2]
        if x3 == 'even':
            al.update(set(x1+x2))
        elif x3 == 'up':
            heav.append(set(x1))
            ligh.append(set(x2))
        else:
            heav.append(set(x2))
            ligh.append(set(x1))
    u=set(heav[0])
    d=set(ligh[0])
    if len(heav)>1:
        for i in heav:
            u=u.intersection(i)
        for i in ligh:
            d=d.intersection(i)
    d=list(d)
    u=list(u)
    for i in u:
        if i not in al and i not in d:
            print(f'{i} is the counterfeit coin and it is heavy. ')
            break
    for i in d:
        if i not in al and i not in u:
            print(f'{i} is the counterfeit coin and it is light. ')
            break












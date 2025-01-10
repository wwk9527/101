pig=[]
a=[10000000]
while True:
    try:
        step=input()
        if step=="pop":
            if len(pig)>0:
                if pig[-1]==a[-1]:
                    a.pop()
                pig.pop()

        elif step=="min":
            if len(pig)>0:
                print(a[-1])
        else:
            l=step.split()
            n=int(l[-1])
            pig.append(n)
            if n<=a[-1]:
                a.append(n)
    except:
        break
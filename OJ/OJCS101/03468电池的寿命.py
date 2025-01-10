while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        j = []
        for i in range(1,n+1):
            j.append(sum(a[0:i] ))
        lex=j[-1]/2
        for x in range(n-1,-1,-1):
            if a[x]<lex and x==n-1:
                break
            elif a[x]<lex and x<n-1:
                lex=j[x]
                break
        print(float(lex))
    except:
        break

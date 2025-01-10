while True:
    n = int(input())
    if n == 0:
        break
    tian = list(map(int, input().split()))
    king = list(map(int, input().split()))
    tian.sort()
    king.sort()
    soc=0
    i=j=0
    si=tj=n-1
    while i<=si:
        if tian[i]>king[j]:
            soc+=200
            i+=1
            j+=1
        elif tian[i]<king[j]:
            soc-=200
            i+=1
            tj-=1
        elif tian[i]==king[j]:
            if tian[si]>king[tj]:
                soc+=200
                si-=1
                tj-=1
            elif tian[si]<king[tj]:
                soc-=200
                i+=1
                tj-=1
            elif tian[si]==king[tj]:
                if tian[i]<king[tj]:
                    soc-=200
                    i+=1
                    tj-=1
                else:
                    soc+=0
                    i+=1
                    tj-=1
    print(soc)









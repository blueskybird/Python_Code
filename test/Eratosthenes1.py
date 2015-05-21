import datetime

def P(n):
    r=int(n**0.5)
    print r
    L=range(1,n+1)
    L[0]=0
    i=2
    while i <= r:
        j=i
        while j*i<=n:
            L[j*i-1]=0
            j+=1
        i+=1
    return L

a=P(30)
print a

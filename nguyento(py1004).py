snt=[True]*10001
def sieve():
    snt[0]=False
    snt[1]=False
    for i in range(2,int(10001**(1/2))):
        if snt[i]:
            for j in range(i*i,10001,i):
                if snt[j]:
                    snt[j]=False
                    
def gdcd(a,b):
    return a if b==0 else gdcd(b,a%b)
def sovle():
    n=int(input())
    cnt=0
    for i in range(n):
        if gdcd(n,i)==1:
            cnt+=1
    return "YES" if snt[cnt] else "NO"
sieve()
for t in range(int(input())):
    print(sovle())
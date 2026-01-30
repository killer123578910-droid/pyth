snt=[1]*10010
def sieve():
    snt[0]=0
    snt[1]=0
    for i in range(2,int(10010**0.5)+1):
        if snt[i]:
            for j in range(i*i,10010,i):
                if snt[j]:
                    snt[j]=0
def sovle():
    n=input()
    inv=int(n[-4:])
    return "YES" if snt[inv] else "NO"
sieve()
for t in range(int(input())):
    print(sovle())
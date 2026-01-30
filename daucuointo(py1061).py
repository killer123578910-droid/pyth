
snt=[1]*1001
def sieve():
    snt[0]=0
    snt[1]=0
    for i in range(2,int(1001**0.5)+1):
        if snt[i]:
            for j in range(i*i,1001,i):
                if snt[j]:
                    snt[j]=0
def sovle():
    n=input()
    dau=int(n[:3])
    cuoi=int(n[-3:])
    return "YES" if snt[dau] and snt[cuoi] else "NO"
sieve()
for t in range(int(input())):
    print(sovle())
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
    for i in range(len(n)):
        if snt[i]:
            if not snt[int(n[i])]:
                return "NO"
        else:
            if snt[int(n[i])]:
                return "NO"
    return "YES"
sieve()
for t in range(int(input())):
    print(sovle())
snte=[0]*10
def snt(n):
    if n<2:
        return 0
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return 0
    return 1
def init():
    for i in range(0,10):
        snte[i]=snt(i)
def sole():
    n=input()
    so=int(n[len(n)-4:len(n)])
    if not snt(len(n)):
        return "NO"
    cnt=0
    for st in n:
        if snte[int(st)]:
            cnt+=1
    return "YES" if cnt>int(len(n)/2) else "NO"
init()
for t in range(int(input())):
    print(sole())
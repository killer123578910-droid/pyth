def snt(n):
    if n<2:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True
def sole():
    n=input()
    so=int(n[len(n)-4:len(n)])
    return "YES" if snt(so) else "NO"
for t in range(int(input())):
    print(sole())
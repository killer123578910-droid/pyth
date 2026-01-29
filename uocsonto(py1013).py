def gdcd(a,b):
    return a if b==0 else gdcd(b,a%b)
def snt(a):
    if a<2:
        return False
    for i in range(2,int(a**1/2)):
        if a%i==0:
            return False
    return True
def solve():
    n,m=map(int,input().split())
    k=str(gdcd(n,m))
    sum=0
    for i in k:
        sum+=int(i)
    return "YES" if snt(sum) else "NO"
for t in range(int(input())):
    print(solve())
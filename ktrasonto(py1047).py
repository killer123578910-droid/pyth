def snt(n):
    if n<2:
        return False
    for i in range(2,(n**(0.5)+1)):
        if n%i==0:
            return False
    return True
def solve():
    n =input()
    so=int(n[len(n)-5:len(n)-1])
    return "YES" if snt(so) else "NO"
for t in range(int(input())):
    print(solve)
    
def snt(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solve():
    n=input()
    summ=0
    for i in n:
        summ+=int(i)
    return "YES" if snt(summ) else "NO"
for t in range(int(input())):
    print(solve())
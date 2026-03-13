import sys
n=int(input())
mx=-10**18
siller=-10**18
for _ in range(n):
    x=int(sys.stdin.readline())
    if x>mx:
        siller=mx
        mx=x
    elif x>siller and x!=mx:
        siller=x
print('Silver =',siller)
        
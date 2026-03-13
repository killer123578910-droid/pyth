import sys
n=int(sys.stdin.readline())
if n==0:
    print(0)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(abs(i-j),end=' ')
    print()
        
t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    x=0
    temp=p
    while temp<=n:
        x+=n//temp
        temp*=p
    print(x)
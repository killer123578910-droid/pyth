fib=[0]*96
def init():
    fib[0]=0
    fib[1]=1
    for i in range(2,94):
        fib[i]=fib[i-1]+fib[i-2]
def sovle():
    a,b=map(int,input().split())
    for i in range(a,b+1):
        print(fib[i],end=' ')
    print()
init()
for t in range(int(input())):
    sovle()
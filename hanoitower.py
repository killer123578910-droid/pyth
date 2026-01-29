def hanoitower(n,a,b,c):
    if n==0:
        return
    hanoitower(n-1,a,c,b)
    print(a+" -> "+c)
    hanoitower(n-1,b,a,c)
n=int(input())
hanoitower(n,"A","B","C")
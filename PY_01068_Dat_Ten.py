n,k=map(int,input().split())
ar=sorted(list(set(input().split())))
n=len(ar)
x=[0]*k
def quailui(i,start):
    for j in range(start,(n-k+i)+1):
        x[i]=ar[j]
        if i==k-1:
            print(*x)
        else:
            quailui(i+1,j+1)
quailui(0,0)
    
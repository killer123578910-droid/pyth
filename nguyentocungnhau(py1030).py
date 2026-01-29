def gdd(a,b):
    return a if b==0 else gdd(b,a%b)
def sovle():
    n,m=map(int,input().split())
    st=10**(m-1)
    end=10**(m)
    cnt=0
    for i in range(st,end):
        if gdd(n,i)==1:
            print(i,end=' ')
            cnt+=1
        if cnt==10:
            print()
            cnt=0
sovle()
        
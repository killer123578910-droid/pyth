def bo0(b):
    for i in range(len(b)):
        if b[i] != '0':
            return b[i:]
    return "0"

            
def bigger(a, b):
    a = bo0(a)
    b = bo0(b)
    if len(a) != len(b):
        return len(a) > len(b)
    return a > b

while True:
    n=int(input())
    if n==0:
        break
    check=False
    minn=maxx=bo0(input())
    pre=minn
    for i in range(n-1):
        k=bo0(input())
        if bigger(k,maxx):
            maxx=k
        if bigger(minn,k):
            minn=k
        if pre!=k:
            check=True
    if check:
        print(minn+' '+maxx)
    else:
        print('BANG NHAU')

    
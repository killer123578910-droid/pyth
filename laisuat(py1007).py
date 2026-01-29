def sovle():
    n,x,m=map(float,input().split())
    ans=0
    while n<m:
        ans+=1
        lai=n*float(x/100)
        n=n+lai
    return ans
for t in range(int(input())):
    print(sovle())
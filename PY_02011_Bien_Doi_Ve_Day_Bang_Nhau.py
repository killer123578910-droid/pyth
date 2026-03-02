n=int(input())
ar=list(map(int,input().split()))
mincost=10000000000
premincost=mincost
median=0
for i in range(len(ar)):
    cost=0
    for j in range(len(ar)):
        cost+=abs(ar[i]-ar[j])
    mincost=min(mincost,cost)
    if premincost!=mincost:
        median=ar[i]
        premincost=mincost
print(str(mincost)+' '+str(median))
    
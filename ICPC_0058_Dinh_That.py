def tarjan(j,ar,vs,v):
    vs[j]=1
    for i in ar[j]:
        if not vs[i]:
            tarjan(i,ar,vs,v)
    return vs[v]

for _ in range(int(input())):
    cnt=0
    n,m,u,v=map(int,input().split())
    ar=[[] for _ in range(n+1)]
    for t in range(m):
        x,y=map(int,input().split())
        ar[x].append(y)
    for dinh in range(1,n+1):
        if dinh !=u and dinh!=v:
            vs=[0]*(n+1)
            vs[dinh]=True
            if not tarjan(u,ar,vs,v):
                cnt+=1
    print(cnt)

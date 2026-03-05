n,m=map(int,input().split())
ar=[]
for i in range(n):
    a=list(map(int,input().split()))
    ar.append(a)
if n==m:
    for i in ar:
        print(*i)
else:
    if n>m:
        deman=abs(n-m)
        cnt=0
        for i in range(0,n):
            if (i+1)%2==0 and cnt!=deman:
                print(*ar[i])
                cnt+=1
            elif cnt>=deman:
                print(*ar[i])
    else:
        deman=abs(n-m)
        mark=[False]*m
        cnt=0
        for j in range(0,m):
            if (j+1)%2==0 and cnt<deman:
                mark[j]=True
                cnt+=1
        for i in range(0,n):
            for j in range(0,m):
                if not mark[j]:
                    print(ar[i][j],end=' ')
            print()
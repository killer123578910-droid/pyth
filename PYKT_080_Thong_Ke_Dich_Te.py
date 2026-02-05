n,m=map(int,input().split())
ar=[[]*m]*n
for i in range(n):
    ar[i]=list(map(int,input().split()))
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
visited = [[False]*m for _ in range(n)]
summ=0
for i in range(n):
    for j in range(m):
        if ar[i][j]==-1:
            for k in range(8):
                ni=i+dx[k]
                nj=j+dy[k]
                if ni<n and nj<m and ni>=0 and nj>=0 and not visited[ni][nj]:
                    summ+=ar[ni][nj]
                    visited[ni][nj]=True
print(summ)

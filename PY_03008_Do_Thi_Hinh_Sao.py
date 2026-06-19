t=int(input())
deg={}
for _ in range(t-1):
    k,l=map(int,input().split())
    if k not in deg:
        deg[k]=0
    if l not in deg:
        deg[l]=0
    deg[k]+=1
    deg[l]+=1
switch=0
for i,j in deg.items():
    if j==t-1:
        switch=1
        break
print("Yes") if switch else print("No")
l,m,k=map(int,input().split())
def pal2(x):
    s=bin(x)[2:]
    return s==s[::-1]
if m==2:
    cnt=0
    for x in range(l,m+1):
        if pal2(x):
            cnt+=1
    print(cnt)
else:
    cnt=0
    if l<=0<=m:
        cnt+=1
    if l<=1<=m:
        cnt+=1
    print(cnt)
        
        
        

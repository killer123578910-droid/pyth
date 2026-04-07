n,m,u=map(int,input().split())
parent=[0]*(n+1)
sz=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
    sz[i]=1

def find(i):
    global parent
    if parent[i]==i:
        return i
    else:
        parent[i]=find(parent[i])
        return parent[i]
def unionn(a,b):
    global parent,sz
    x1=find(a)
    x2=find(b)
    if(x1==x2):
        return
    else:
        if sz[x1]<sz[x2]:
            x1,x2=x2,x1
        sz[x1]+=sz[x2]
        parent[x2]=x1
for i in range(m):
    a,b=map(int,input().split())
    unionn(a,b)
for i in range(1,n+1):
    if find(i)!=find(u):
        print(i)
        
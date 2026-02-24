leng=[0]*93
leng[1]=1
for i in range(2,93):
    leng[i]=leng[i-1]*2+1
def kitu(n,k):
    mid=leng[n]//2
    mid+=1
    if k<mid:
        return kitu(n-1,k)
    if k>mid:
        return kitu(n-1,k-mid)
    if k==mid:
        return chr(ord('A')+(n-1))
for t in range(int(input())):
    n,k=map(int,input().split())
    print(kitu(n,k))
        
    
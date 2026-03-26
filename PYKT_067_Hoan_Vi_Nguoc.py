n=0
ar=[]
flag=1
def init():
    global ar,n
    ar=[0]*(n+1)
    for i in range(1,n+1): ar[i]=i
def sinhhoanvi():
    global ar,flag,n
    i=n-1
    while i>0 and ar[i]>ar[i+1]:
       i-=1
    if i==0:
      flag=0
    else:
        j=n
        while ar[j]<ar[i]:
            j-=1
        ar[i],ar[j]=ar[j],ar[i]
        d,c=i+1,n
        while d<c:
            ar[d],ar[c]=ar[c],ar[d]
            d+=1
            c-=1
for _ in range(int(input())):
    n=int(input())
    init()
    flag=1
    ans=[]
    while flag:
        ans.append(ar[:])
        sinhhoanvi()
    print(len(ans))
    for i in range(len(ans)-1,-1,-1):
        for j in range(1,n+1):
            print(ans[i][j],end='')
        print(end=' ')
    print()
        
        
def sovle():
    a,k,n= map(int,input().split())
    cnt=0;
    for i in range(1,n-a+1):
        if (a+i)%k==0:
            print(i,end=" ")
            cnt+=1
    if cnt==0: print("-1")
    else: print()
sovle()
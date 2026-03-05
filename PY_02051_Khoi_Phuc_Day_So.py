n,a,s=int(input()),[],0
for i in range(n):
    arr=list(map(int,input().split()))
    s+=sum(arr)
    a.append(arr)
#suma1-an=2*suma
tongkq=s//((n-1)*2)
#sum[a1]=a1+a2+a1+a3+a1+a4+a1+a5+...
#(n-1)*a1+(a1+a2+a3+....-a1)=(n-2)a1+tongkq=>a1=(sum[a1]-tongkq)//(n-2)
if n==2:
    print('1'+' '+str((s//2)-1))
else:
    x1=(sum(a[0])-tongkq)//(n-2)
    print(x1,end=' ')
    for i in range(1,n):
        print(a[0][i]-x1,end=' ')
for _ in range(int(input())):
    n=int(input())
    def cmp(a,b):
        return a[1]<b[1];
    ar=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        ar.append(temp)
    ar.sort(key=lambda x:x[1])
    cnt=1
    pre=ar[0][1]
    for i in ar:
        if i[0]>=pre:
            cnt+=1
            pre=i[1]
    print(cnt)
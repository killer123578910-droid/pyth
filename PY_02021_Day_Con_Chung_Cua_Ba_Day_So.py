for t in range(int(input())):
    n,k,m=map(int,input().split())
    ar1=list(map(int,input().split()))
    ar2=list(map(int,input().split()))
    ar3=list(map(int,input().split()))
    i=l=j=0
    ans=[]
    while i<n and l<k and j<m:
        maxcur=max(ar1[i],ar2[l],ar3[j])
        if ar1[i]==ar2[l]==ar3[j]:
           ans.append(ar1[i])
           i+=1
           j+=1
           l+=1
        if l<k and ar2[l]<maxcur:
            l+=1
        if i<n and ar1[i]<maxcur:
            i+=1
        if j<m and ar3[j]<maxcur:
            j+=1
    if ans:
        print(*ans)
    else:
        print('NO')

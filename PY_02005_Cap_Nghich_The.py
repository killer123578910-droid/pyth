def nghichthe(a):
    if len(a)<=1:
        return a,0
    mid=len(a)//2
    left,idxl=nghichthe(a[:mid])
    right,idxr=nghichthe(a[mid:])
    merge=[]
    i=j=0
    inv=idxl+idxr
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merge.append(left[i])
            i+=1
        else:
            merge.append(right[j])
            inv+=len(left)-i
            j+=1
    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge,inv
n=int(input())
a=list(map(int,input().split()))
print(nghichthe(a)[1])

import heapq
for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    freq={}
    for i in ar:
        if i not in freq:
            freq[i]=0
        freq[i]+=1
    q=[]
    dodai=len(ar)//2
    for item,re in freq.items():
        if re>dodai:
            heapq.heappush(q,(re,item))
    if not q:
        print("NO")
    else:
        re,item=heapq.heappop(q)
        print(item)
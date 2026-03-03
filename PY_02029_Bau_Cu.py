import heapq
n,m=map(int,input().split())
ar=list(map(int,input().split()))
freq={}
sett=set()
qeue=[]
for i in ar:
    if i not in freq:
        freq[i]=0
    freq[i]+=1
group={}
for item,val in freq.items():
    if val not in group:
        group[val]=[]
    group[val].append(item)
ans={}
for val,it in group.items():
    ans[min(it)]=val
for it,val in ans.items():
    heapq.heappush(qeue,(-val,it))
if len(qeue)<2:
    print("NONE")
else:
    heapq.heappop(qeue)
    val,kq=heapq.heappop(qeue)
    print(kq)

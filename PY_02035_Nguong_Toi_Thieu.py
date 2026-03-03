import heapq
n=input()
k=int(input())
nl=len(n)
i=0
dic={}
while i<nl and i+1<nl:
    temp=int(n[i:i+2])
    if temp not in dic:
        dic[temp]=0
    dic[temp]+=1
    i+=2
ans=[]
for item,val in dic.items():
    if val>=k:
        heapq.heappush(ans,(item,val))
if not ans:
    print("NOT FOUND")
else:
    while ans:
        it,val=heapq.heappop(ans)
        print(str(it)+" "+str(val))
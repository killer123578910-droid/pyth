import heapq
n = int(input())
ar = []

while len(ar) < n:
    ar.extend(list(map(int, input().split())))
le=[]
chan=[]
for i in ar:
    if i%2==0:
        heapq.heappush(chan,i)
    else:
        heapq.heappush(le,-i)
for i in ar:
    if i%2==0:
        print(heapq.heappop(chan),end=' ')
    else:
        print(-heapq.heappop(le),end=' ')
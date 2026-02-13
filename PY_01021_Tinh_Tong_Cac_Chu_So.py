import heapq
def sovle():
    n=input()
    ans=[]
    summ=0
    i=0
    while i<len(n):
        if n[i].isdigit():
            summ+=int(n[i])
        else:
            heapq.heappush(ans,n[i])
        i+=1
    while ans:
        print(heapq.heappop(ans),end='')
    print(summ)
for k in range(int(input())):
    sovle()

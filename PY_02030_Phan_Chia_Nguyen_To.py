MAX = 1001
snt = [1] * (MAX + 1)
snt[0] = snt[1] = 0

for i in range(2, int(MAX**0.5) + 1):
    if snt[i]:
        for j in range(i*i, MAX + 1, i):
            snt[j] = 0
n=int(input())
ar=list(map(int,input().split()))
dictt={}
for i in ar:
    if i not in dictt:
        dictt[i]=1
ar=list(dictt)
prefix=[0]*len(ar)
prefix[0]=ar[0]
for i in range(1,len(ar)):
    prefix[i]=prefix[i-1]+ar[i]
for i in len(ar):
    if snt[prefix[i]] and snt[prefix[len(ar)-1]-prefix[i]]:
        print(i)
        break


MAX = 20000
snt = [1] * (MAX + 1)
snt[0] = snt[1] = 0

for i in range(2, int(MAX**0.5) + 1):
    if snt[i]:
        for j in range(i*i, MAX + 1, i):
            snt[j] = 0

n=int(input())
ar=list(map(int,input().split()))
snte=[]
for i in ar:
    if snt[i]:
        snte.append(i)
snte.sort()
j=i=0
while i<len(ar):
    if snt[ar[i]]:
        print(snte[j],end=' ')
        j+=1
    else:
        print(ar[i],end=' ')
    i+=1

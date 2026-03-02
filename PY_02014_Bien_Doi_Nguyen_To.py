MAX = 20000

snt = [1] * (MAX + 1)
snt[0] = snt[1] = 0

for i in range(2, int(MAX**0.5) + 1):
    if snt[i]:
        for j in range(i*i, MAX + 1, i):
            snt[j] = 0

def nearsnt(n):
    if snt[n]:
        return 0
    
    d = 1
    while True:
        if n - d >= 2 and snt[n - d]:
            return d
        if n + d <= MAX and snt[n + d]:
            return d
        d += 1

n = int(input())
ar = list(map(int, input().split()))

ans = 0
for x in ar:
    ans=max(ans,nearsnt(x))

print(ans)

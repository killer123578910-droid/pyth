n, K = map(int, input().split())
ar = list(map(int, input().split()))

ar.sort()

groups = 1

for i in range(1, n):
    if ar[i] - ar[i-1] > K:
        groups += 1

print(groups)
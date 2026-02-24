n = set(input().lower().split())
k = set(input().lower().split())

print(*sorted(n | k))
print(*sorted(n & k))

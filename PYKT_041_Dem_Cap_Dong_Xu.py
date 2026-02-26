n = int(input())
grid = [input().strip() for _ in range(n)]

ans = 0

for i in range(n):
    cnt = grid[i].count('C')
    ans += cnt * (cnt - 1) // 2

for j in range(n):
    cnt = 0
    for i in range(n):
        if grid[i][j] == 'C':
            cnt += 1
    ans += cnt * (cnt - 1) // 2

print(ans)

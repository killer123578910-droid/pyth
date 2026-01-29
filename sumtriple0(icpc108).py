import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    cnt = 0
    for i in range(n-2):
        l,r=i+1,n-1
        while l < r:
            s = a[i] + a[l] + a[r]
            if not s:
                cnt += 1
                l += 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    print(cnt)

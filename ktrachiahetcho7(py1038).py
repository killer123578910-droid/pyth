def solve(n, inv, timee):
    if int(n)%7==0:
        return n
    kq = int(n) + int(inv)
    if kq % 7 == 0:
        return str(kq)
    if timee >= 1000:
        return "-1"
    inv = str(kq)[::-1]
    return solve(kq, inv, timee + 1)

for _ in range(int(input())):
    n = input().strip()
    print(solve(n, n[::-1], 1))

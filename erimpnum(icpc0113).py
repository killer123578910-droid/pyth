snt = [1] * 100001

def sieve():
    snt[0] = snt[1] = 0
    for i in range(2, int(100001**0.5) + 1):
        if snt[i]:
            for j in range(i*i, 100001, i):
                snt[j] = 0

def solve():
    n = int(input())
    st = 13
    ans = []

    while st < n:
        if snt[st]:
            dao = int(str(st)[::-1])
            if dao < n and dao < len(snt) and snt[dao] and st < dao:
                ans.append(st)
                ans.append(dao)
        st += 1

    print(*ans)

sieve()
for _ in range(int(input())):
    solve()

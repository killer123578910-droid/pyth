from collections import deque
def solve():
    n=int(input())
    ar=list(map(int, input().split()))
    stack=deque()
    ans=[0]*len(ar)
    for i in range(0,len(ar)):
        while stack and ar[stack[-1]]<=ar[i]:
            stack.pop()
        if not stack:
            ans[i]=i+1
        else:
            ans[i]=i-stack[-1]
        stack.append(i)
    print(*ans)
for _ in range(int(input())):
    solve()
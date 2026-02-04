def solve():
    n=[]
    while len(n)<10:
        n.extend(map(int,input().split()))
    ans=set()
    for i in n:
        ans.add(i%42)
    print(len(ans))
solve()
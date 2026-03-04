def solve():
    n = input()
    while len(n) > 1:
        nk = len(n)
        mid = nk // 2
        sum1=int(n[:mid])
        sum2=int(n[mid:])
        
        n = str(sum1 + sum2)
        print(n)

solve()
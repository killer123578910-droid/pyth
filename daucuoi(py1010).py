def solve():
    n=input()
    so1=n[0:2]
    so2=n[len(n)-2:len(n)]
    return "YES" if so1==so2 else "NO"
for t in range(int(input())):
    print(solve())
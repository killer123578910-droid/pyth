def solve():
    n=input()
    return "YES" if n[0]==n[len(n)-1] else "NO"
for t in range(int(input())):
    print(solve())
def solve():
    n=input().strip()
    ans=n.split('.')
    if len(ans)!=4:
        return "NO"
    else:
        for i in ans:
            if i =="" or not i.isdigit() or int(i)<0 or int(i)>255:
                return "NO"
        return "YES"

for t in range(int(input())):
    print(solve())
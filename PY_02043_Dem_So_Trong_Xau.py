def solve():
    n=input()
    s=input()
    k=len(s)
    cnt=0
    j=0
    while j<=len(n)-k:
        if n[j:j+k]==s:
            cnt+=1
            j+=k
        else:
            j+=1
    return cnt
for t in range(int(input())):
    print(solve())
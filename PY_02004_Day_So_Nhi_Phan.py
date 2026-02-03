def solve():
    k=input()
    n=list(map(int,input().split()))
    cnt=0
    for i in range(1,len(n)):
        if n[i]!=n[i-1]:
            cnt+=1
    return cnt
print(solve())
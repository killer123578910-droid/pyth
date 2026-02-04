def sovle():
    n=int(input())
    ar1=list(map(int,input().split()))
    ar2=list(map(int,input().split()))
    ar1.sort()
    ar2.sort()
    for i in range(n):
        if ar1[i]>ar2[i]:
            return "NO"
    return "YES"
for t in range(int(input())):
    print(sovle())
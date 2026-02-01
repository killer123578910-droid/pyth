def sovle():
    n,m=map(int, input().split())
    ar=list(map(int,input().split()))
    idx=m%n
    for i in range(idx,len(ar)):
        print(ar[i],end=" ")
    for i in range(idx):
        print(ar[i],end=' ')
    print()
for t in range(int(input())):
    sovle()
    
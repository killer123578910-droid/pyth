n,m=map(int,input().split())
ar1=set(map(int,input().split()))
ar2=set(map(int,input().split()))
print("YES" if sorted(ar1)==sorted(ar2) else "NO")

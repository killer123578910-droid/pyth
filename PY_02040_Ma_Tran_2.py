n=int(input())
ar=[]
for i in range(n):
    ar.append(input().split())
k=int(input())
add1=0
add2=0
for i in range(n):
    for j in range(n):
        if i+j<n-1:
            add1+=int(ar[i][j])
        elif i+j>n-1:
            add2+=int(ar[i][j])
ans=abs(add1-add2)
print("YES" if ans<=k else "NO")
print(ans)

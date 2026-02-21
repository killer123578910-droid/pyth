n=int(input())
ar=set(map(int,input().split()))
flag=0
for i in range(1,n+1):
    if i not in ar:
        print(i)
        flag=1
        break
if not flag:
    print(n+1)
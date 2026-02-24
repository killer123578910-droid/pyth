import math
n=int(input())
ar=sorted(list(map(int,input().split())))
for i in range(0,n-1):
    for j in range(i+1,n):
        if math.gcd(ar[i],ar[j])==1:
            print(str(ar[i])+' '+str(ar[j]))

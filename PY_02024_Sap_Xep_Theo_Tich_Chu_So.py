import math
def digit_sum(x):
        m=1
        for i in str(x):
            m*=int(i)
        return m
def sovle():
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort(key=lambda x:(digit_sum(x),x))
    print(*ar)
for _ in range(int(input())):
    sovle()
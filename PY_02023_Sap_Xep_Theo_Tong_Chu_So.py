def digit_sum(x):
        return sum(int(d) for d in str(x))
def sovle():
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort(key=lambda x:(digit_sum(x),x))
    print(*ar)
for _ in range(int(input())):
    sovle()
x = [0]*21
ar = []

def qlui(i):
    global n, k
    for j in range(x[i-1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            for l in range(1, k+1):
                print(ar[x[l]-1], end=" ")
            print()
        else:
            qlui(i+1)

n, k = map(int, input().split())
ar = sorted(set(map(int, input().split())))
n = len(ar)

qlui(1)

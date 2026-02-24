def sove(ar):
    cnt = 0
    while True:
        if ar[0] == ar[1] == ar[2] == ar[3]:
            return cnt
        
        new_ar = [
            abs(ar[0] - ar[1]),
            abs(ar[1] - ar[2]),
            abs(ar[2] - ar[3]),
            abs(ar[3] - ar[0])
        ]
        
        ar = new_ar
        cnt += 1


while True:
    ar = list(map(int, input().split()))
    if ar == [0,0,0,0]:
        break
    print(sove(ar))
def cv(x, a):
    if x == 0:
        return [0]
    res = []
    while x > 0:
        res.append(x % a)
        x //= a
    return res

def ispal(arr):
    return arr == arr[::-1]

while True:
    try:
        n = input().strip()
        if not n:
            continue
        if n == '-1':
            break
        
        x, a, b = map(int, n.split())
        
        sa = cv(x, a)
        sb = cv(x, b)
        
        if ispal(sa) and ispal(sb):
            print("YES")
        else:
            print("NO")
    except:
        break
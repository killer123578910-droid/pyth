def sovle():
    n=input()
    for i in range(10):
        if i==4 or i==7:
            continue
        else:
            if str(i) in n:
                return False
    return True
for t in range(int(input())):
    print("YES" if sovle() else "NO")
    
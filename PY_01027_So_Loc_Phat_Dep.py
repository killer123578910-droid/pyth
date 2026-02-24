n = input()
i = 0
ok = True

while i < len(n):
    if n[i] != '6':
        ok = False
        break
    i += 1
    
    count8 = 0
    while i < len(n) and n[i] == '8':
        count8 += 1
        if count8 > 2:
            ok = False
            break
        i += 1
    
    if not ok:
        break

print("YES" if ok else "NO")

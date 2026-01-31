def sovle():
    n=input()
    inv=n[::-1]
    for i in range(1,len(n)):
        if abs(ord(n[i])-ord(n[i-1]))!=abs(ord(inv[i])-ord(inv[i-1])):
            return "NO"
    return "YES"
for t in range(int(input())):
    print(sovle())
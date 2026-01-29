def sovle():
    x=input()
    temp=list(x)
    inv=temp[::-1]
    for i in range(1,len(temp)):
        if abs(ord(temp[i])-ord(temp[i-1]))!=abs(ord(inv[i])-ord(inv[i-1])):
            return "NO"
    return "YES"
for t in range(int(input())):
    print(sovle())
    
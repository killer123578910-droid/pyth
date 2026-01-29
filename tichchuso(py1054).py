def sovle():
    n=input()
    tich=1
    for i in n:
        if i=='0':
            continue
        else:
            tich*=int(i)
    return tich
for t in range(int(input())):
    print(sovle())
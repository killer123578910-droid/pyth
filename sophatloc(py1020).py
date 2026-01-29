def sovle():
    x=input()
    return "YES" if (x[len(x)-2]+x[len(x)-1])=='86' else 'NO'
for t in range(int(input())):
    print(sovle())

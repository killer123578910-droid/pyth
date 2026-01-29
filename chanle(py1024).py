def sovle():
    x=input()
    summ=0
    for i in range(1,len(x)):
        if abs(int(x[i])-int(x[i-1]))!=2:
            return "NO"
        summ+=int(x[i-1])
    summ+=int(x[len(x)-1])
    return "YES" if summ%10==0 else "NO"
for t in range(int(input())):
    print(sovle())
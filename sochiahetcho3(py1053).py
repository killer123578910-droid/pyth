def sovle():
    n=input()
    summ=0
    for i in n:
        summ+=int(i)
    return "YES" if summ%3==0 else "NO"
for t in range(int(input())):
    print(sovle())
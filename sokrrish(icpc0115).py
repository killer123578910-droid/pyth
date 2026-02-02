fab=[0]*11
def factorial():
    fab[0]=1
    for i in range(1,10):
        fab[i]=fab[i-1]*i
def sovle():
    n=input()
    kq=0
    for i in n:
        kq+=fab[int(i)]
    return "Yes" if kq==int(n) else "No"
factorial()
for t in range(int(input())):
    print(sovle())
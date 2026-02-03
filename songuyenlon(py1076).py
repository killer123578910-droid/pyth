def modst(b,a):
    r=0
    for ch in b:
        r=(r*10+int(ch))%a
    return r
def gcde(a,b):
    while a!=0:
        b,a=a,modst(b,a)
        b=str(b)
    return int(b)

def sovle():
    a=int(input())
    b=input()
    return gcde(a,b)
for t in range(int(input())):
    print(sovle())

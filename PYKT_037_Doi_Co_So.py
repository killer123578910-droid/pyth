so={}
x='A'
for i in range(10,36):
    so[i]=x
    x=chr(ord(x)+1)
def sovle():
    n,b=map(int,input().split())
    k=n
    coso2=""
    while k>0:
        temp=k%b
        if temp>=10:
            temp=so[temp]
        coso2=str(temp)+coso2
        k//=b
    return coso2
for t in range(int(input())):
    print(sovle())
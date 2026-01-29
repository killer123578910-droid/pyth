def gdd(a,b):
    return a if b==0 else gdd(b,a%b)
def sovle():
    x=input()
    temp=list(x)
    inv="".join(temp[::-1])
    return "YES" if gdd(int(x),int(inv))==1 else "NO"
for t in range(int(input())):
    print(sovle())
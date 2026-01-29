def sovle():
    n=input()
    if len(n)%2==0:
        return "NO"
    if n[0]==n[1]:
        return "NO"
    for i in range(0,len(n),2):
        if n[i]!=n[len(n)-1]:
            return "NO"
    return "YES"
for t in range(int(input())):
    print(sovle())
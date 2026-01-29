p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    x=input().split()
    if  x[0]=='0':
        break
    k=int(x[0])
    if len(x)==1:
        s=list(input())
    else:
        s=list(x[1])
    for i in range(len(s)):
        idx=p.index(s[i])
        s[i]=p[(idx+k)%28]
    print("".join(s[::-1]))


t=int(input())
while t>0:
    st=input()
    temp=""
    maxx=0
    for c in st:
        if c.isdigit():
            temp+=c
        else:
            if temp:
                maxx=max(maxx,int(temp))
                temp=""
    if temp:
        maxx=max(maxx,int(temp))
    print(maxx,end="\n")
    t-=1    
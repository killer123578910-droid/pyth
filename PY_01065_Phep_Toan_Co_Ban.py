def genk(a):
    ar=[]
    if a[0]=='?':
        for i in range(1,10):
            ar.append(str(i)+a[1:])
    else: ar.append(a)
    r=[]
    if a[1]=='?':
        for i in ar:
            for j in range(0,10):
                r.append(i[0]+str(j))
    else: r=ar
    return r

def genop(a):
    if a=="?":
        return "+-*/"
    else: return [a]

for _ in range(int(input())):
    a1,op,a2,eq,ans=input().split()
    a1=genk(a1)
    op=genop(op)
    a2=genk(a2)
    ans=genk(ans)
    ok=0
    an1=op1=an2=ans2=""
    for i in a1:
        for j in op:
            for k in a2:
                for l in ans:
                    if j=='+': 
                        ok=(int(i)+int(k)==int(l))
                        an1,op1,an2,ans2=i,j,k,l
                    if j=='-': 
                        ok=(int(i)-int(k)==int(l))
                        an1,op1,an2,ans2=i,j,k,l
                    if j=='*': 
                        ok=(int(i)*int(k)==int(l))
                        an1,op1,an2,ans2=i,j,k,l
                    if j=='/'and int(i)%int(k)==0: 
                        ok=(int(i)//int(k)==int(l))
                        an1,op1,an2,ans2=i,j,k,l
                    if ok: break
                if ok: break
            if ok: break
        if ok:break
    print(f'{an1} {op1} {an2} = {ans2}') if ok else print("WRONG PROBLEM!")
def solan(n):
    sola=1 if len(n)==1 else 0
    while len(n)>1:
        summ=0
        for i in n:
            summ+=int(i)
        sola+=1
        n=str(summ)
    return sola
n=input()
ans=''
if not n[0].isdigit():
    ans=n[1:]
else:
    ans=n
print(solan(ans))

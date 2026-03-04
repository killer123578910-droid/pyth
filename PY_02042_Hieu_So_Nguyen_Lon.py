n1=input().lstrip('0') or '0'
n2=input().lstrip('0') or '0'
negative = False
if len(n1) < len(n2) or (len(n1) == len(n2) and n1 < n2):
    n1, n2 = n2, n1
    negative = True
l=max(len(n1),len(n2))
n1=n1.zfill(l)
n2=n2.zfill(l)    
ans=''
l1=l2=len(n1)
carry=0
for i in range(l-1,-1,-1):
    k1=int(n1[i])
    k2=int(n2[i])+carry
    if k1-k2<0:
        tempans=str(10+k1-k2)
        carry=1
    else:
        tempans=str(k1-k2)
        carry=0
    ans=tempans+ans
ans=ans.lstrip('0') or '0'
if negative and ans!='0':
    ans='-'+ans
print(ans)
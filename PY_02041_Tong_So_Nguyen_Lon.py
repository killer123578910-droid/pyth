n1=input()
n2=input()
l1=len(n1)
l2=len(n2)
while len(n1)!=len(n2):
    if l1<l2:
        n1='0'+n1
    else:
        n2='0'+n2     
ans=''
l1=l2=len(n1)
j=l1-1
k=l2-1
carry=0
for i in range(l2,0,-1):
    tempans=int(n1[j])+int(n2[k])+carry
    if tempans>9:
        carry=1
        ans=str(tempans)[1]+ans
    else:
        carry=0
        ans=str(tempans)+ans
    j-=1
    k-=1
if carry:
    ans='1'+ans
print(ans.lstrip('0') or '0')
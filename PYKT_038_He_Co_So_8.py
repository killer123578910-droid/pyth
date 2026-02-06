def tinh(n):
    ans = 0
    j = 0
    for i in range(len(n) - 1, -1, -1):
        ans += int(n[i]) * (2 ** j)
        j += 1
    return str(ans)


n=input()
temp=''
ans=''
for i in range(len(n)-1,-1,-1):
    temp=n[i]+temp
    if len(temp)==3:
        ans=tinh(temp)+ans
        temp=''
if len(temp)==3:
    ans=tinh(temp)+ans
elif len(temp)>0:
    if len(temp) > 0:
        temp = temp.zfill(3)
    ans=tinh(temp)+ans
else:
    pass
print(ans)
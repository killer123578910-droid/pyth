n=input()
def buoc(s):
    if len(s)==1:return 0
    sum=0
    for i in s:sum+=ord(i)-ord('0')
    return 1+buoc(str(sum))
if len(n)<=1:print(1)
else:print(buoc(n))
n=input()
nl=len(n)
i=0
dic={}
while i<nl and i+1<nl:
    temp=int(n[i:i+2])
    if temp not in dic:
        dic[temp]=1
    i+=2
ar=list(dic.fromkeys(dic))
print(*ar)
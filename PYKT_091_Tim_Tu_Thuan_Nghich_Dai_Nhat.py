def thuannghich(n):
    return n==n[:-1]
f=open("VANBAN.in",'r')
dic={}
maxlen=0
chose=''
for i in f:
    k=i.split()
    for e in k:
        if(thuannghich(e) and maxlen<len(e)):
            if e not in dic:
                dic[e]=0
            dic[e]+=1
            chose=e
            maxlen=len(e)
print(chose+" "+str(dic[chose]))
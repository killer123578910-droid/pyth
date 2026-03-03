n=input()
nl=len(n)
i=0
dic={}
while i<nl and i+1<nl:
    temp=int(n[i:i+2])
    if temp not in dic:
        dic[temp]=0
    dic[temp]+=1
    i+=2
for item,val in dic.items():
    print(str(item)+' '+str(val))
n=list(input().split())
maxx=0
maxxre=''
for i in n:
    if len(i)>maxx:
        maxx=len(i)
        maxxre=i
print(maxxre+' '+str(maxx))        

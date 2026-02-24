k=int(input())
for i in range(k):
    n1=input()
    n2=input()
    print("Test "+str(i+1)+': ',end='')
    flag=False
    dic1={}
    dic2={}
    if len(n1)!=len(n2):
        print("NO")
    else:
        for k in n1:
            if k not in dic1:
                dic1[k]=0
            dic1[k]+=1
        for e in n2:
            if e not in dic2:
                dic2[e]=0
            dic2[e]+=1 
        if dic1!=dic2:
            print("NO")
        else:
            print("YES")   
    
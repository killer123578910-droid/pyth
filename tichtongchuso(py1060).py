def sovle():
    n=input()
    cnt=0
    tong=0
    tich=1
    for i in range(len(n)):
        if i%2!=0:
            tong+=int(n[i])
        else:
            if int(n[i])!=0:
                tich*=int(n[i])
                cnt=1
    if cnt==0:
        tich=0
    print(str(tich)+" "+str(tong))
for t in range(int(input())):
    sovle()
    
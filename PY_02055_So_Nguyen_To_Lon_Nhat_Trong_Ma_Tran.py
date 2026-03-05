MaX=1001
snt=[1]*MaX
for i in range(2,int(MaX**(0.5))+1):
    if snt[i]:
        for j in range(i*i,MaX,i):
            if snt[j]:
                snt[j]=0
snt[0]=snt[1]=0
n,m=list(map(int,input().split()))
ar=[]
for i in range(0,n):
    ar.append(list(map(int,input().split())))
maXsnt=0
for i in range(0,n):
    for j in range(0,m):
        if snt[ar[i][j]]:
            maXsnt=max(maXsnt,ar[i][j])
if not maXsnt:
    print('NOT FOUND')
else:
    print(maXsnt)
    for i in range(0,n):
        for j in range(0,m):
            if ar[i][j]==maXsnt:
                print('Vi tri '+'['+str(i)+']'+'['+str(j)+']')

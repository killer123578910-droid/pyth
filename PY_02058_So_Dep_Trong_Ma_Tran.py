n,m=list(map(int,input().split()))
ar=[]
for i in range(0,n):
    ar.append(list(map(int,input().split())))
maXsnt=-1
minsnt=100001
for i in range(0,n):
    for j in range(0,m):
        maXsnt=max(maXsnt,ar[i][j])
        minsnt=min(minsnt,ar[i][j])
mm=maXsnt-minsnt
flag=0
for i in ar:
    if mm in i:
        flag=1
        break
if not flag:
    print("NOT FOUND")
else:
    print(mm)
    for i in range(0,n):
        for j in range(0,m):
            if ar[i][j]==mm:
                print('Vi tri '+'['+str(i)+']'+'['+str(j)+']')

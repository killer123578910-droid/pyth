def thuannghich(n):
    if n<10:
        return False
    temp=str(n)
    for i in range(len(temp)//2):
        if temp[i]!=temp[len(temp)-1-i]:
            return False
    return True
n,m=list(map(int,input().split()))
ar=[]
for i in range(0,n):
    ar.append(list(map(int,input().split())))
maXsnt=-1
for i in range(0,n):
    for j in range(0,m):
        if thuannghich(ar[i][j]):
            maXsnt=max(maXsnt,ar[i][j])
if maXsnt==-1:
    print('NOT FOUND')
else:
    print(maXsnt)
    for i in range(0,n):
        for j in range(0,m):
            if ar[i][j]==maXsnt:
                print('Vi tri '+'['+str(i)+']'+'['+str(j)+']')

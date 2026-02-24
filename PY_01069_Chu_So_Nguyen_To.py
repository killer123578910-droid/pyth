n=int(input())
x=[0]*(n+1)
ar=[2,3,5,7]

cnt1=0
cnt2=0
cnt3=0
cnt4=0
def check():
    if x[n]==2:
        return False
    return cnt1 and cnt2 and cnt3 and cnt4
def quaylui(i):
    global cnt1,cnt2,cnt3,cnt4
    for j in ar:
        old1,old2,old3,old4=cnt1,cnt2,cnt3,cnt4
        x[i]=j
        if x[i]==2:
            cnt1=1
        if x[i]==3:
            cnt2=1
        if x[i]==5:
            cnt3=1
        if x[i]==7:
            cnt4=1
        if i==n:
            if check():
                for l in range(1,n+1):
                    print(x[l],end='')
                print()
                
        else:
            quaylui(i+1)
        cnt1, cnt2, cnt3, cnt4 = old1, old2, old3, old4
k=n
for i in range(4,k+1):
    n=i
    quaylui(1)
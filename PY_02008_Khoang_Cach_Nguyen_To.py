snt=[1]*100001
def sieve():
    snt[0]=0
    snt[1]=0
    for i in range(2,int(100001**(1/2))+1):
        if snt[i]:
            for j in range(i*i,100001,i):
                if snt[j]:
                    snt[j]=0
sieve()
n, x = [int(i) for i in input().split()]
ans=[x]
prime=[]
for i in range(2,100001):
    if snt[i]:
        prime.append(i)
for i in range(0,n):
    temp=ans[i]+prime[i]
    ans.append(temp)
for i in ans:
    print(i,end=' ')
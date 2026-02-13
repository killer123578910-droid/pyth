n=int(input())
limit=int(n**0.5)+1
snt=[1]*limit
snt[0]=0
snt[1]=0
primes=[]
for i in range(2,limit):
    if snt[i]:
        primes.append(i)
        for j in range(i*i,limit,i):
            if snt[j]:
                snt[j]=0
k=0
cnt=0
while k < len(primes) and primes[k]**8<=n:
    cnt+=1
    k+=1
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if primes[i]*primes[j]<=n**(0.5):
            cnt+=1

print(cnt)
     
    
snt=[1]*100001
def sieve():
    for i in range(2,int(100001**(1/2))):
        if snt[i]:
            for j in range(i*i,100001,i):
                if snt[j]:
                    snt[j]=0

def sovle():
    x=int(input())
    freq={}
    n=x
    for i in range(2,int(x**(1/2))+1):
        if snt[i] and n%i==0:
            if i not in freq:
                freq[i]=0
            while n%i==0:
                freq[i]+=1
                n//=i
    if n>1:
        if n not in freq:
            freq[n]=1
        else:
            freq[n]+=1
    ans='1'
    for i,n in freq.items():
        ans=ans+' * '+str(i)+"^"+str(n)
    return ans
sieve()
for t in range(int(input())):
    print(sovle())
                
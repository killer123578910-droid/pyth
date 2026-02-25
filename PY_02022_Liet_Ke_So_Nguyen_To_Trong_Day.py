def snt(n):
    if n<2: return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True
n=int(input())
ar=list(map(int,input().split()))
freq=dict()
for i in ar:
    if snt(i):
        if i not in freq:
            freq[i]=0
        freq[i]+=1
for items,values in freq.items():
    print(str(items)+" "+str(values))
    
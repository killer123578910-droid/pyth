N=10**18
liste=[]
i=1
while i<=N:
    j=1
    while i*j<=N:
        k=1
        while i*j*k<=N:
            liste+=[i*j*k]
            k*=5
        j*=3
    i*=2
liste.sort()
def se(n,l,r):
    if l>r:
        return "Not in sequence"
    mid=l+(r-l)//2
    if n==liste[mid]:
        return mid+1
    elif n<liste[mid]:
        return se(n,l,mid-1)
    else:
        return se(n,mid+1,r)
def sovle():
    n=int(input())
    print(se(n,0,len(liste)))
for t in range(int(input())):
    sovle()

        
        
n=input()
nl=len(n)
i=0
ar=set()
while i<nl and i+1<nl:
    ar.add(int(n[i:i+2]))
    i+=2
ar=sorted(ar)
print(*ar)
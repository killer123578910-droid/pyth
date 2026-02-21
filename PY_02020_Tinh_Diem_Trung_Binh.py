n=int(input())
ar=list(map(float,input().split()))
maxx=0
minn=11
for i in ar:
    maxx=max(maxx,i)
    minn=min(minn,i)
for i in ar:
    if i==maxx:
        ar.remove(i)
    if i==minn:
        ar.remove(i)
summ=0
for i in ar:
    summ+=i
print('{:.2f} '.format(summ/len(ar)))
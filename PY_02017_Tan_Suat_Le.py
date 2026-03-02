def sovel():
    n=int(input())
    ar=list(map(int,input().split()))
    freq={}
    for i in ar:
        if i not in freq:
            freq[i]=0
        freq[i]+=1
    for items,value in freq.items():
        if value%2!=0:
            print(items)
            break
for t in range(int(input())):
    sovel()


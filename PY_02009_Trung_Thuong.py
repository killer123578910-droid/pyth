def solve():
    n=int(input())
    freq={}
    for i in range(n):
        temp=int(input())
        if temp not in freq:
            freq[temp]=0
        freq[temp]+=1
    freqmax=0
    nummax=0
    for num,fr in freq.items():
        if fr>freqmax:
            nummax=num
            freqmax=fr
        elif fr==freqmax:
            nummax=min(num,nummax)
        else:
            pass
    return nummax
for t in range(int(input())):
    print(solve())
            
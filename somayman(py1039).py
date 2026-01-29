def sovle():
    n=input()
    freq={}
    pre='.'
    for i in range(0,len(n)):
        if i not in freq:
            freq[n[i]]=0
        freq[n[i]]+=2
        if pre==n[i]:
            return "NO"
        else:
            pre=n[i]
    return "YES" if len(freq)==2 else "NO"
for t in range(int(input())):
    print(sovle())

        
def sovle():
    n=input()
    freq={}
    keyy=''
    for i in n:
        if not i.isdigit():
            keyy=i
            if keyy not in freq:
                freq[keyy]=0
        else:
            freq[keyy]=int(i)
    for i,n in freq.items():
        print(str(i)*n,end='')
    print()
for t in range(int(input())):
    sovle()
    
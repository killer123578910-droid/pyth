def sovle():
    n=input()+'!'
    pre=''
    cnt=1
    for ch in n:
        if ch==pre:
            cnt+=1
        elif pre!='':
            print(str(cnt)+pre,end='')
            cnt=1
        pre=ch
    print()
for t in range(int(input())):
    sovle()


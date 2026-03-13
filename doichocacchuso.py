def prev_per(s):
    a=list(s)
    n=len(a)
    i=n-2
    while i>=0 and a[i]<=a[i+1]:
        i-=1
    if i==-1:
        return '-1'
    j=n-1
    while a[j]>=a[i]:
        j-=1
    while j>i+1 and a[j]==a[j-1]:
        j-=1
    a[i],a[j]=a[j],a[i]

    if a[0]=='0':
        return '-1'
    return ''.join(a)
for _ in range(int(input())):
    n=input()
    print(prev_per(n))
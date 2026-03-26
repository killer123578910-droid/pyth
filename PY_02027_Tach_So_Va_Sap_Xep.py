n=int(input())
ar=[]
for k in range(n):
    st=input()
    i=0
    while i<len(st):
        if st[i].isdigit():
            temp=''
            while i<len(st) and st[i].isdigit():
                temp+=st[i]
                i+=1
            temp=temp.lstrip('0') or '0'
            ar.append(int(temp))
        if i<len(st): i+=1
for i in sorted(ar):
    print(i)
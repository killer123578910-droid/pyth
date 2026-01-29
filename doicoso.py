def bintobase(s, base):
    k={2:1,4:2,8:3,16:4}[base]
    while len(s)%k!=0:
        s='0'+s
    digits="0123456789ABCDEF"
    res=""
    for i in range(0,len(s),k):
        group=s[i:i+k]
        val=0
        for bit in group:
            val=val*2+int(bit)
        res=res+digits[val]
    return res.lstrip("0")    
        
t=int(input())
while t>0:
    base=int(input())
    st=input()
    print(bintobase(st,base))
    t-=1
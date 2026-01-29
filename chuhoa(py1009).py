def sold():
    freq={}
    n=input()
    cnt=0
    for i in n:
        if i.isupper():
            cnt+=1
    if(len(n)/2<cnt):
        print(n.upper())
    else:
        print(n.lower())
sold()

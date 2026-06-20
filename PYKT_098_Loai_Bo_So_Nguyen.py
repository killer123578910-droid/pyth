import re
with open("DATA.in",'r',encoding='utf-8') as f:
    data=f.read()
    listt=data.split()
    kq=[]
    for i in listt:
        #if not i: continue
        try:
            num=int(i)
            if not (-2**31-1<=num<=2**31-1):
                kq.append(i)
        except:
            kq.append(i)
    print(*sorted(kq))
from datetime import datetime
def dayb(d1,d2):
    dfor="%d/%m/%Y"
    k1=datetime.strptime(d1,dfor)
    k2=datetime.strptime(d2,dfor)
    return abs(k2-k1).days
class hoadon:
    def __init__(self,ma='',ten='',mp='',tg=0,dg=0):
        self.ma=ma
        self.ten=ten
        self.mp=mp
        self.tg=tg
        self.dg=dg
    def out(self):
        return f'{self.ma} {self.ten} {self.mp} {self.tg} {self.dg}'

ar=[]
bac={1:25,2:34,3:50,4:80}
for t in range(int(input())):
    tk=hoadon()
    k=str(t+1)
    while len(k)<2:
        k='0'+k
    tk.ma="KH"+k
    tk.ten=input().strip()
    tk.mp=input().strip()
    st1=input().strip()
    en1=input().strip()
    tk.tg=dayb(st1,en1)+1
    pp=int(input())
    tk.dg=bac[int(tk.mp[0])]*tk.tg+pp
    ar.append(tk)
ar.sort(key=lambda x:(-x.dg))
for i in ar:
    print(i.out())    
    
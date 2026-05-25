from datetime import datetime
def turnday(a):
    dfor='%d/%m/%Y'
    k1=datetime.strptime(a,dfor)
    return k1
class rac:
    def __init__(self,ma='',theloai='',ntn='',ten='',sotap=0):
        self.ma=ma
        self.theloai=theloai
        self.ntn=ntn
        self.ten=ten
        self.sotap=sotap
    def out(self):
        return f'{self.ma} {self.theloai} {self.ntn} {self.ten} {self.sotap}'
ar=[]
theloai={}
n,m=map(int,input().split())
for t in range(n):
    tl=input()
    k=str(t+1)
    while(len(k)<3):
        k='0'+k
    ma='TL'+k
    theloai[ma]=tl
for t in range(m):
    tk=rac()
    kl=str(t+1)
    while(len(kl)<3):
        kl='0'+kl
    tk.ma='P'+kl
    tl=input().strip()
    tk.theloai=theloai[tl]
    tk.ntn=input().strip()
    tk.ten=input().strip()
    tk.sotap=int(input())
    ar.append(tk)
ar.sort(key=lambda x:(turnday(x.ntn),x.ten,-x.sotap))
for i in ar:
    print(i.out())


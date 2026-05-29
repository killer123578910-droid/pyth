def chuanhoa(en):
    return ' '.join(en.split()).title()
class sucvat:
    def __init__(self,maob='',ten='',diem=0.0,xephang=0):
        self.maob=maob
        self.ten=ten
        self.diem=diem
        self.xephang=xephang
    def out(self):
        return f'{self.maob} {self.ten} {self.diem:.2f} {self.xephang}'
ar=[]
for _ in range(int(input())):
    tk=sucvat()
    ma=str(_+1)
    while(len(ma)<2):
        ma='0'+ma
    tk.maob='SV'+ma
    tk.ten=chuanhoa(input())
    d1=int(input())
    d2=int(input())
    d3=int(input())
    tk.diem=((d1*3+d2*3+d3*2)/8)+1e-8
    ar.append(tk) 
ar.sort(key=lambda x:(-x.diem,x.maob))

ar[0].xephang=1
cnt=1
for i in range(1,len(ar)):
    if ar[i].diem==ar[i-1].diem:
        ar[i].xephang=ar[i-1].xephang
        cnt+=1
    else:
        ar[i].xephang=ar[i-1].xephang+cnt
        cnt=1
for i in ar:
    print(i.out())
        
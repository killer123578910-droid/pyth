class thisinh:
    def __init__(self,ma='',ten='',mon='',diem=0.0):
        self.ma=ma
        self.ten=ten
        self.mon=mon
        self.diem=diem
    def out(self):
        gc=''
        if self.diem>=18:
            gc='TRUNG TUYEN'
        else:
            gc='LOAI'
        return f'{self.ma} {self.ten} {self.mon} {self.diem:.1f} {gc}'
ar=[]
mon={'A':"TOAN",'B':"LY",'C':"HOA"}
diemut={'1':2.0,'2':1.5,'3':1.0,'4':0.0}
for t in range(int(input())):
    tk=thisinh()
    k=str(t+1)
    while(len(k)<2):
        k='0'+k
    tk.ma='GV'+k
    tk.ten=input()
    ma=input().strip()
    tk.mon=mon[ma[0]]
    tin=float(input())
    cm=float(input())
    tk.diem=((tin*2+cm))+diemut[ma[1]]
    ar.append(tk)
ar.sort(key=lambda x:(-x.diem,x.ma))
for i in ar:
    print(i.out())
    
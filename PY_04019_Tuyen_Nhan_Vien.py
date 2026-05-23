class nhanvien:
    def __init__(self,ma='',ten='',dtb=0.0):
        self.ma=ma
        self.ten=ten
        self.dtb=dtb
    def out(self):
        thuhang=""
        kq = round(self.dtb + 1e-8, 2)
        if kq<5.0:
            thuhang="TRUOT"
        elif(5.0<=kq<8.0):
            thuhang="CAN NHAC"
        elif(8.0<=kq<9.5):
            thuhang="DAT"
        elif(kq>=9.5):
            thuhang="XUAT SAC"
        return f'{self.ma} {self.ten} {self.dtb:.2f} {thuhang}'
    
ar=[]
for t in range(int(input())):
    tk=nhanvien()
    k=str(t+1)
    tk.ma='TS0'+k
    tk.ten=input()
    lt=float(input())
    th=float(input())
    if lt>10:
        lt/=10
    if th>10:
        th/=10
    tk.dtb=(lt+th)/2
    ar.append(tk)
ar.sort(key=lambda x:(-x.dtb,x.ma))
for i in ar:
    print(i.out())    
       
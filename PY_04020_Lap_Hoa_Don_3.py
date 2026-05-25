class hoadon:
    def __init__(self,ma='',ten='',soluong=0,dgia=0,chkhau=0,tongtien=0):
        self.ma=ma
        self.ten=ten
        self.soluong=soluong
        self.dgia=dgia
        self.chkhau=chkhau
        self.tongtien=tongtien
    def out(self):
        return f'{self.ma} {self.ten} {self.soluong} {self.dgia} {self.chkhau} {self.tongtien}'
ar=[]
for t in range(int(input())):
    tk=hoadon()
    tk.ma=input()
    tk.ten=input()
    tk.soluong=int(input())
    tk.dgia=int(input())
    tk.chkhau=int(input())
    tk.tongtien=(tk.soluong*tk.dgia)-tk.chkhau
    ar.append(tk)
ar.sort(key=lambda x:(-x.tongtien,x.ma))
for i in ar:
    print(i.out())
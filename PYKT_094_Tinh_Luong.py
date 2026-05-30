class nhanvien:
    def __init__(self,manv='',ten='',phb='',lt=0):
        self.manv=manv
        self.ten=ten
        self.phb=phb
        self.lt=lt
    def out(self):
        return f"{self.manv} {self.ten} {self.phb} {self.lt}"

ar=[]
mph={}
bl={'A':[10,12,14,20],
    'B':[10,11,13,16],
    'C':[9,10,12,14],
    'D':[8,9,11,13]}
n=int(input())
for i in range(n):
    li=list(map(str,input().split()))
    mph[li[0]]=" ".join(li[1:])
m=int(input())
for i in range(m):
    tk=nhanvien()
    tk.manv=input().strip()
    tk.phb=mph[tk.manv[-2:]]
    tk.ten=input().strip()
    luongcb=int(input().strip())*1000
    ngaycong=int(input())
    thamnien=int(tk.manv[1:3])
    if 1<=thamnien<=3:
        thamnien=0
    elif 4<=thamnien<=8:
        thamnien=1
    elif 9<=thamnien<=15:
        thamnien=2
    else:
        thamnien=3
    tk.lt=luongcb*ngaycong*bl[tk.manv[0]][thamnien]
    ar.append(tk)
for i in ar:
    print(i.out())
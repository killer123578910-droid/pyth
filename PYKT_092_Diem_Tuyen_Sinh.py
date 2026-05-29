def chuanhoa(en):
    return ' '.join(en.split()).title()
class nhanvien:
    def __init__(self,maob='',ten='',diem=0.0):
        self.maob=maob
        self.ten=ten
        self.diem=diem
    def out(self):
        gc=''
        if self.diem>=20.5: gc="Do"
        else: gc='Truot'
        return f'{self.maob} {self.ten} {self.diem:.1f} {gc}'
ar=[]
dic={1:1.5,2:1,3:0}
for i in range(int(input())):
    tk=nhanvien()
    ma=str(i+1)
    while(len(ma)<2):
        ma='0'+ma
    tk.maob="TS"+ma
    tk.ten=chuanhoa(input())
    tk.diem=float(input())
    dantoc=input()
    if dantoc!="Kinh":
        tk.diem+=1.5
    kv=int(input())
    tk.diem+=dic[kv]
    ar.append(tk)
ar.sort(key=lambda x:(-x.diem,x.maob))
for i in ar:
    print(i.out())
def chuna(st):
    return " ".join(st.split()).title()
class nhanvien:
    def __init__(self,manv='',ten='',trondm=0,vuotdm=0,thue=0,tong=0):
        self.manv=manv
        self.ten=ten
        self.trondm=trondm
        self.vuotdm=vuotdm
        self.thue=thue
        self.tong=tong
    def out(self):
        return f"{self.manv} {self.ten} {self.trondm} {self.vuotdm} {self.thue} {self.tong}"
ar=[]
dm={'A':100,'B':500,'C':200}
for i in range(int(input())):
    tk=nhanvien()
    ma=str(i+1)
    while(len(ma)<2):
        ma='0'+ma
    tk.manv='KH'+ma
    tk.ten=chuna(input().strip())
    loai,st,en=map(str,input().split())
    tong=int(en)-int(st)
    if tong<=dm[loai]:
        tk.trondm=tong*450
        tk.vuotdm=0
        tk.thue=0
    else:
        tk.trondm=dm[loai]*450
        tk.vuotdm=(tong-dm[loai])*1000
        tk.thue=int((tk.vuotdm*0.05)+1e-8)
    tk.tong=tk.trondm+tk.vuotdm+tk.thue
    ar.append(tk)
ar.sort(key=lambda x:-x.tong)
for i in ar:
    print(i.out())
    



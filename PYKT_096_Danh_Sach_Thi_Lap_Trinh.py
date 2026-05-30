class sv:
    def __init__(self,manv='',ten='',tt='',tentr=''):
        self.manv=manv
        self.ten=ten
        self.tt=tt
        self.tentr=tentr
    def out(self):
        return f"{self.manv} {self.ten} {self.tt} {self.tentr}"
ar=[]
motrg={}
gantg={}

for i in range(int(input())):
    team=input().strip()
    trg=input().strip()
    motrg[team]=trg
    ma=str(i+1)
    while(len(ma)<2):
        ma='0'+ma
    temp="Team"+ma
    gantg[temp]=team
for i in range(int(input())):
    tk=sv()
    ma1=str(i+1)
    while(len(ma1)<3):
        ma1='0'+ma1
    tk.manv="C"+ma1
    tk.ten=input().strip()
    tm=input().strip()
    tk.tt=gantg[tm]
    tk.tentr=motrg[tk.tt]
    ar.append(tk)
ar.sort(key=lambda x:(x.ten))
for i in ar:
    print(i.out())
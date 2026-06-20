class monthi:
    def __init__(self,mamon,tenmon,hinhthuc):
        self.mamon,self.tenmon,self.hinhthuc=mamon,tenmon,hinhthuc
    def out(self):
        return f'{self.mamon} {self.tenmon} {self.hinhthuc}'

ar=[]
for _ in range(int(input())):
    tk=monthi("","","")
    tk.mamon=input().strip()
    tk.tenmon=input().strip()
    tk.hinhthuc=input().strip()
    ar.append(tk)

ar.sort(key=lambda x:(x.mamon))
for i in ar:
    print(i.out())
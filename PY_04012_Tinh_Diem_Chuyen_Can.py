class studen:
    def __init__(self,ten='',malop='',chuyencan=10,ghichu=''):
        self.ten=ten
        self.malop=malop
        self.chuyencan=chuyencan
        self.ghichu=ghichu
    def out(self):
        if self.chuyencan<=0:
            return f'{self.ten} {self.malop} {self.chuyencan} {self.ghichu}'
        return f'{self.ten} {self.malop} {self.chuyencan}'

ar=dict()    
for t in range(int(input())):
    tk=studen()
    masv=input()
    tk.ten=input()
    tk.malop=input()
    ar[masv]=tk
for i in range(len(ar)):
    mas,key=map(str,input().split())
    for k in key:
        if k=='m':
            ar[mas].chuyencan-=1    
        elif k=='v':
            ar[mas].chuyencan-=2
    if ar[mas].chuyencan<=0: 
        ar[mas].chuyencan=0
        ar[mas].ghichu="KDDK"
for kj,li in ar.items():
    print(kj+" "+li.out())
    
    
            
            

        
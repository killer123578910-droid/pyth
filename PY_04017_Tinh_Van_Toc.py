class runer:
    def __init__(self,ma='',ten='',dc='',td=0):
        self.ma=ma
        self.ten=ten
        self.dc=dc
        self.td=td
    def out(self):
        return f'{self.ma} {self.ten} {self.dc} {round(self.td)} Km/h'
ar=[]
for t in range(int(input())):
    tk=runer()
    tk.ten=input().strip()
    tk.dc=input().strip()
    tachten=list(map(str,tk.ten.split()))
    tachdc=list(map(str,tk.dc.split()))
    kk=''
    lk=''
    for i in tachten:
        kk+=i[0]
    for i in tachdc:
        lk+=i[0]
    tk.ma=lk+kk
    en1,en2=map(int,input().split(':'))
    en1=en1*60+en2
    moc=6*60
    if moc>en1:
        en1+=24*60
    tg=en1-moc
    tg/=60
    tk.td=120/tg
    ar.append(tk)
ar.sort(key=lambda x:(-x.td,x.ma))
for i in ar:
    print(i.out())
class rah:
    def __init__(self,ma='',ten='',tg=0):
        self.ma=ma
        self.ten=ten
        self.tg=tg
    def out(self):
        gio=self.tg//60
        phut=self.tg%60
        hr=f'{gio} gio {phut} phut'
        return f'{self.ma}  {self.ten} {hr}'

ar=[]
for t in range(int(input())):
    tk=rah()
    tk.ma=input()
    tk.ten=input()
    sth,stp=map(int,input().split(":"))
    endt,endp=map(int,input().split(":"))
    stp=sth*60+stp
    endp=endt*60+endp
    if endp<stp:
        endp+=24*60
    tk.tg=endp-stp
    ar.append(tk)

ar.sort(key=lambda x:-x.tg)
for i in ar:
    print(i.out())
    
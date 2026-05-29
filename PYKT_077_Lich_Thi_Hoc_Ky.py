from datetime import datetime
def day(st):
    return datetime.strptime(st,"%d/%m/%Y")
def gio(st):
    le1,le2=map(int,st.split(":"))
    return le1*60+le2
class lichthi:
    def __init__(self,maob='',mamon='',tenmon='',ngay='',gio='',nhomthi=''):
        self.maob=maob
        self.mamon=mamon
        self.tenmon=tenmon
        self.ngay=ngay
        self.gio=gio
        self.nhomthi=nhomthi
    def out(self):
        return f'{self.maob} {self.mamon} {self.tenmon} {self.ngay} {self.gio} {self.nhomthi}'

ar=[]
dicmamon={}
n,m=map(int,input().split())
for i in range(n):
    k=input()
    l=input()
    dicmamon[k]=l
    
for _ in range(m):
    tk=lichthi()
    ma=str(_+1)
    while(len(ma)<3):
        ma='0'+ma
    tk.maob='T'+ma
    tk.mamon,tk.ngay,tk.gio,tk.nhomthi=map(str,input().split())
    tk.tenmon=dicmamon[tk.mamon]
    ar.append(tk)
ar.sort(key=lambda x:(day(x.ngay),gio(x.gio),x.mamon))
for i in ar:
    print(i.out())
    
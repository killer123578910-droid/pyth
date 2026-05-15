class hoadon:
    def __init__(self,ma='',ten='',cs=0):
        self.ma=ma
        self.ten=ten
        self.cs=cs
    def thanhtien(self):
        if 0<=self.cs<51:
            tien=self.cs*100
            return round(tien+(tien*(2/100)))
        elif 51<=self.cs<101:
            hight=self.cs-50
            tien=((50*100)+(hight*150))*1.03
            return round(tien)
        elif self.cs>=100:
            hight=self.cs-100
            tien=((50*100)+(50*150)+(hight*200))*1.05
            return round(tien)
    def out(self):
        return self.ma+" "+self.ten+" "+str(self.thanhtien())
ar=[]
for t in range(int(input())):
    tk=hoadon()
    temp=str(t+1)
    while len(temp)<2:
        temp='0'+temp
    tk.ma="KH"+temp
    tk.ten=input()
    a=[]
    while len(a)<2:
        a.extend(list(map(int,input().split())))
    tk.cs=a[1]-a[0]
    ar.append(tk)
ar.sort(key=lambda x:(-x.thanhtien(),x.ma))
for i in ar:
    print(i.out())

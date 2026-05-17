class pupil:
    def __init__(self,ma="",ten='',d=[]):
        self.ma=ma
        self.ten=ten
        self.d=d

    def tb(self):
        summ=2*(self.d[0]+self.d[1])
        for i in range(2,len(self.d)):
            summ+=self.d[i]
        return summ/12
    def out(self):
        thuhang=""
        kq = round(self.tb() + 1e-8, 1)
        if kq<5.0:
            thuhang="YEU"
        elif(5.0<=kq<7.0):
            thuhang="TB"
        elif(7.0<=kq<8.0):
            thuhang="KHA"
        elif(8.0<=kq<9.0):
            thuhang="GIOI"
        elif(kq>=9.0):
            thuhang="XUAT SAC"
        return self.ma+" "+self.ten+" "+ f'{kq:.1f}' +" "+thuhang
ar=[]
for t in range(int(input())):
    n1=pupil()
    temp=str(t+1)
    while len(temp)<2:
        temp='0'+temp
    n1.ma="HS"+temp
    n1.ten=input()
    ke=[]
    while len(ke)<10:
        ke.extend(list(map(float,input().split())))
    n1.d=ke
    ar.append(n1)
ar=sorted(ar,key=lambda x:(-x.tb(),x.ma))

for i in ar:
    print(i.out())

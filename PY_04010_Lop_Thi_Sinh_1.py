class thising:
    def __init__(self,ten="",boy="",p1=0,p2=0,p3=0):
        self.ten=ten
        self.boy=boy
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def out(self):
        diem=f'{(self.p1+self.p2+self.p3):.1f}'
        return self.ten+" "+self.boy+" "+diem
te=thising()
te.ten=input()
te.boy=input()
te.p1=float(input())
te.p2=float(input())
te.p3=float(input())
print(te.out())
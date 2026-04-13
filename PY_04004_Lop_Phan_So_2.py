import math
class phanso:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau 
    def rutgon(self):
        dgc=math.gcd(self.tu,self.mau)
        self.tu/=dgc
        self.mau/=dgc
        print(str(int(self.tu))+'/'+str(int(self.mau)))
    def __add__(self,other):
        self.tu=self.tu*other.mau+self.mau*other.tu
        self.mau=self.mau*other.mau
        return self
        
arr=list(map(int,input().split()))
r1=phanso(arr[0],arr[1])
r2=phanso(arr[2],arr[3])
tong=r1+r2
tong.rutgon()
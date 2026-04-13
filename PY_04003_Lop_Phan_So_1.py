import math
class phanso:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau 
    def rutgon(self):
        dgc=math.gcd(self.tu,self.mau)
        self.tu/=dgc
        self.mau/=dgc
        print(str(int(self.tu))+"/"+str(int(self.mau)))
arr=list(map(int,input().split()))
r=phanso(arr[0],arr[1])
r.rutgon()
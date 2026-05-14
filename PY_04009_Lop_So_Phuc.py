class complex:
    def __init__(self,thuc,ao):
        self.thuc=thuc
        self.ao=ao
    def out(self):
        if(self.ao<0):
          return str(self.thuc) + " - "+str(abs(self.ao))+"i"
        return str(self.thuc) + " + " +str(self.ao)+"i"
    def __add__(self, other):
        kq=complex(0,0)
        kq.thuc=self.thuc+other.thuc
        kq.ao=self.ao+other.ao
        return kq
    def __mul__(self, other):
        kq=complex(0,0)
        kq.thuc=self.thuc*other.thuc-self.ao*other.ao
        kq.ao=self.ao*other.thuc+self.thuc*other.ao
        return kq
    
data = list(map(int, open(0).read().split()))

t = data[0]
idx = 1

for _ in range(t):
    a, b, c, d = data[idx:idx+4]
    idx += 4
    a1=complex(a,b)
    a2=complex(c,d)
    
    kq1=(a1+a2)*a1
    kq2=(a1+a2)*(a1+a2)
    
    print(kq1.out()+', '+kq2.out())
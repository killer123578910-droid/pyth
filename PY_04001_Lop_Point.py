class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def distance(self,p2):
        kq=round(((p2.a-self.a)**2+(p2.b-self.b)**2)**(1/2),4)
        return (f"{kq:.4f}")
def Decimal(a):
        return float(a)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
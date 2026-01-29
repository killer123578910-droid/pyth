import math
def sovle():
    l,r=map(int, input().split())
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            for l in range(j+1,r+1):
                if math.gcd(i,j)==1 and math.gcd(i,l)==1 and math.gcd(j,l)==1:
                    print("({}, {}, {})".format(i,j,l))
sovle()
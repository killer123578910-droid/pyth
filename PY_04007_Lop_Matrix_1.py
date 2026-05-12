class matrix:
    def __init__(self,a,b,ar):
        self.a=a
        self.ar=ar
        self.b=b

    def __mul__(self, other):

        kq = [[0 for _ in range(other.b)] for _ in range(self.a)]

        for i in range(self.a):
            for j in range(other.b):
                for k in range(self.b):
                    kq[i][j] += self.ar[i][k] * other.ar[k][j]

        return matrix(self.a, other.b, kq)

    def tichnghich(self):

        invar = [[0 for _ in range(self.a)] for _ in range(self.b)]

        for i in range(self.a):
            for j in range(self.b):
                invar[j][i] = self.ar[i][j]

        temp = matrix(self.b, self.a, invar)

        return self * temp


for t in range(int(input())):

    n,m = map(int,input().split())

    ar = []

    while(len(ar) < n):
        ar.append(list(map(int,input().split())))

    cur = matrix(n,m,ar)

    ans = cur.tichnghich()

    for i in ans.ar:                        
        print(*i)
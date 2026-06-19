ep=1e-8
class pont:
    def __init__(self,p1,p2):
        self.p1,self.p2=p1,p2
def dientich(a,b,c):
    D = a.p1*(b.p2-c.p2) + b.p1*(c.p2-a.p2) + c.p1*(a.p2-b.p2)
    if abs(D)<ep:
        return None
    return 2.0*D




for _ in range(int(input())):
    n=int(input())
    k=int(input())
    ar=[]
    for i in range(n):
        nn,mm=map(int,input().split()) 
        ar.append(pont(nn,mm))
    ok=0
    for i in range(n):
        for j in range(i+1,n):
            for k1 in range(j+1,n):
                D=dientich(ar[i],ar[j],ar[k1])
                if D is not None:
                    Ux=((ar[i].p1*ar[i].p1+ ar[i].p2*ar[i].p2)*(ar[j].p2-ar[k1].p2)
                        +(ar[j].p1*ar[j].p1+ ar[j].p2*ar[j].p2)*(ar[k1].p2-ar[i].p2)
                        +(ar[k1].p1*ar[k1].p1+ ar[k1].p2*ar[k1].p2)*(ar[i].p2-ar[j].p2))/D
                    Uy=((ar[i].p1*ar[i].p1+ ar[i].p2*ar[i].p2)*(ar[k1].p1-ar[j].p1)
                        +(ar[j].p1*ar[j].p1+ ar[j].p2*ar[j].p2)*(ar[i].p1-ar[k1].p1)
                        +(ar[k1].p1*ar[k1].p1+ ar[k1].p2*ar[k1].p2)*(ar[j].p1-ar[i].p1))/D
                    R=(Ux-ar[i].p1)*(Ux-ar[i].p1)+(Uy-ar[i].p2)*(Uy-ar[i].p2)
                    cnt=0
                    for z in ar:
                        if z==ar[i] or z==ar[j] or z==ar[k1]:
                            continue
                        d2=(Ux-z.p1)*(Ux-z.p1)+(Uy-z.p2)*(Uy-z.p2)
                        if d2<R-ep:
                            cnt+=1
                            if cnt>k:
                                break
                    if cnt==k:
                        ok=1
                        break
            if ok == 1:
                break # Thoát vòng lặp j
        if ok == 1:
            break # Thoát vòng lặp i
    print("YES") if ok else print("NO")
                    
                
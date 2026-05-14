class tram:
    def __init__(self,ten='',tg='',lm=0):
        self.ten=ten
        self.lm=lm
        self.tg=tg
    def out(self):
        return self.ten+" "+ self.tb()
    def tb(self):
        kq=self.lm/self.tg
        return f'{kq:.2f}'
        
    


ar=[]
for t in range(int(input())):
    ten=input()
    h1,h2=map(int,input().split(":"))
    p1,p2=map(int,input().split(":")) 
    lm=float(input())
    h2=h1*60+h2
    p2=p1*60+p2
    if p2<h2:
        p2+=24*60
    diff=(p2-h2)/60
    flag=1
    for i in ar:
        if i.ten==ten:
            i.tg+=diff
            i.lm+=lm
            flag=0
            break  
    if flag:
        temp=tram(ten,diff,lm)
        ar.append(temp)

for i in range(len(ar)):
    nametag=str(i+1)
    while len(nametag)<2:
        nametag="0"+nametag    
    nametag="T"+nametag
    print(nametag+" "+ar[i].out())
    
      
    
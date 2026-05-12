import math

def dis(a,b): return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
t=int(input())
l=[]
for i in range(t):
    l.extend(float(x) for x in input().split())
i=0
for j in range(t):
    a=dis([l[i],l[i+1]],[l[i+2],l[i+3]])
    b=dis([l[i],l[i+1]],[l[i+4],l[i+5]])
    c=dis([l[i+4],l[i+5]],[l[i+2],l[i+3]])
    i+=6
    if max([a,b,c])*2 >= a+b+c: print("INVALID")
    else:
        kq=0.25*(math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b)))
        print(f'{round(kq,3):.2f}')